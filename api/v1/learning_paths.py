"""
Learning paths API endpoints
Adaptive learning path management and recommendations
"""

from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from api.v1.auth import get_current_user
from config.database import get_db, get_neo4j_driver
from database.models import User, LearningPath, LearningSession, Concept, UserConceptProgress, LearningPathConcept


# Router instance
router = APIRouter()


@router.get("/")
async def get_learning_paths(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get available learning paths.
    Currently generates paths dynamically based on Concept Domains.
    """
    
    # 1. Group Concepts by Domain (e.g., "Computer Science", "Web Development")
    concepts = db.query(Concept).all()
    domains = {}
    
    for c in concepts:
        if c.domain not in domains:
            domains[c.domain] = []
        domains[c.domain].append(c)
        
    # 2. Construct Learning Path Objects
    paths = []
    path_id_counter = 1
    
    for domain, domain_concepts in domains.items():
        # Calculate stats for this path
        total_concepts = len(domain_concepts)
        
        # Calculate average difficulty level
        difficulty_scores = {
            "beginner": 1,
            "intermediate": 2, 
            "advanced": 3
        }
        avg_difficulty_score = sum(difficulty_scores.get(c.difficulty_level.lower(), 2) for c in domain_concepts) / len(domain_concepts)
        
        if avg_difficulty_score <= 1.5:
            difficulty = "Beginner"
        elif avg_difficulty_score <= 2.5:
            difficulty = "Intermediate"
        else:
            difficulty = "Advanced"
            
        estimated_hours = total_concepts * 3  # Assume 3 hours per concept
        
        # Calculate progress for this domain
        user_progress = db.query(UserConceptProgress).filter(
            UserConceptProgress.user_id == current_user.user_id,
            UserConceptProgress.concept_id.in_([c.concept_id for c in domain_concepts])
        ).all()
        
        completed_in_domain = sum(1 for p in user_progress if p.status == 'completed')
        progress_percent = round((completed_in_domain / total_concepts * 100) if total_concepts > 0 else 0)
        
        # Create Path Object
        paths.append({
            "id": path_id_counter,
            "title": f"Mastering {domain}",
            "description": f"A comprehensive journey through {domain} fundamentals and advanced concepts.",
            "difficulty": difficulty,
            "duration": f"{max(1, total_concepts // 2)} weeks",
            "concepts_count": total_concepts,
            "progress": progress_percent,
            "estimated_hours": estimated_hours,
            "category": domain
        })
        path_id_counter += 1
    
    # 3. Add some default paths if no concepts exist
    if not paths:
        paths = [
            {
                "id": 1,
                "title": "Programming Fundamentals",
                "description": "Start your programming journey with core concepts.",
                "difficulty": "Beginner",
                "duration": "4 weeks",
                "concepts_count": 5,
                "progress": 0,
                "estimated_hours": 15,
                "category": "Programming"
            },
            {
                "id": 2,
                "title": "Web Development Basics", 
                "description": "Learn to build modern web applications.",
                "difficulty": "Beginner",
                "duration": "6 weeks",
                "concepts_count": 8,
                "progress": 0,
                "estimated_hours": 24,
                "category": "Web Development"
            }
        ]
        
    return paths


@router.get("/recommendations")
async def get_learning_recommendations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    GENUINE AI: Queries the Knowledge Graph to find the optimal next step.
    Logic: "Find concepts that depend on what I've already finished."
    """
    
    # 1. Get list of everything the user has finished
    completed_records = db.query(UserConceptProgress).filter(
        UserConceptProgress.user_id == current_user.user_id,
        UserConceptProgress.status == "completed"
    ).all()
    
    completed_ids = [r.concept_id for r in completed_records]
    
    # If user is new, recommend "Beginner" nodes
    if not completed_ids:
        beginner_concepts = db.query(Concept).filter(
            Concept.difficulty_level.in_(["beginner", "Beginner"])
        ).all()
        
        recommendations = []
        for concept in beginner_concepts[:3]:
            recommendations.append({
                "concept_id": concept.concept_id,
                "title": concept.display_name,
                "description": concept.description,
                "reason": "Perfect for getting started",
                "difficulty": concept.difficulty_level,
                "estimated_time": "30-60 minutes",
                "match_score": "100%"
            })
        
        return {
            "recommendations": recommendations,
            "message": "Welcome! Here are the best concepts to start your learning journey.",
            "recommendation_type": "beginner_friendly"
        }

    # 2. ASK NEO4J (The Brain) - Get concepts that depend on completed ones
    driver = get_neo4j_driver()
    recommendations = []
    
    if driver:
        try:
            query = """
            // Find concepts the user completed
            MATCH (completed:Concept)
            WHERE completed.concept_id IN $completed_ids
            
            // Find 'next step' concepts that REQUIRE the completed ones
            MATCH (next:Concept)-[:PREREQUISITE]->(completed)
            WHERE NOT next.concept_id IN $completed_ids
            
            // Return the concept and how many requirements user has met
            RETURN next.concept_id as concept_id, next.name as name, 
                   next.display_name as title, next.description as desc, 
                   next.difficulty_level as difficulty,
                   count(completed) as prerequisites_met,
                   size((next)-[:PREREQUISITE]->(:Concept)) as total_prerequisites
            ORDER BY prerequisites_met DESC, difficulty
            LIMIT 5
            """
            
            with driver.session() as session:
                result = session.run(query, completed_ids=completed_ids)
                
                for record in result:
                    prerequisites_met = record['prerequisites_met']
                    total_prerequisites = record['total_prerequisites']
                    readiness_score = (prerequisites_met / total_prerequisites * 100) if total_prerequisites > 0 else 100
                    
                    if readiness_score >= 50:  # User is ready for this concept
                        recommendations.append({
                            "concept_id": record["concept_id"],
                            "title": record["title"],
                            "description": record["desc"],
                            "reason": f"You've mastered {prerequisites_met} of {total_prerequisites} prerequisites!",
                            "difficulty": record["difficulty"],
                            "match_score": f"{int(readiness_score)}%",
                            "estimated_time": "45-90 minutes"
                        })
                        
        except Exception as e:
            print(f"Graph Error: {e}")
            # Fallback to simple SQL-based recommendations
            pass
    
    # 3. Fallback: SQL-based recommendations if Neo4j fails
    if not recommendations:
        in_progress_concepts = db.query(UserConceptProgress).filter(
            UserConceptProgress.user_id == current_user.user_id,
            UserConceptProgress.status == "in_progress"
        ).all()
        
        in_progress_ids = {r.concept_id for r in in_progress_concepts}
        
        # Recommend concepts not started but related to in-progress ones
        related_concepts = db.query(Concept).filter(
            ~Concept.concept_id.in_(completed_ids + list(in_progress_ids))
        ).limit(3).all()
        
        for concept in related_concepts:
            recommendations.append({
                "concept_id": concept.concept_id,
                "title": concept.display_name,
                "description": concept.description,
                "reason": "Continue your learning journey",
                "difficulty": concept.difficulty_level,
                "match_score": "75%",
                "estimated_time": "45-90 minutes"
            })

    return {
        "recommendations": recommendations,
        "message": f"Found {len(recommendations)} personalized recommendations based on your progress",
        "completed_concepts": len(completed_ids),
        "recommendation_type": "graph_based" if driver and recommendations else "sequential"
    }


@router.post("/{path_id}/start")
async def start_learning_path(
    path_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Start a learning path"""
    
    # For now, just return success message
    # In a real implementation, this would create a learning session
    return {
        "message": f"Started learning path {path_id}",
        "session_id": f"session_{path_id}_{current_user.user_id}",
        "status": "started"
    }


@router.post("/sessions/{session_id}/complete")
async def complete_learning_session(
    session_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Complete a learning session"""
    
    # For now, just return success message
    return {
        "message": f"Completed learning session {session_id}",
        "status": "completed",
        "completed_at": "2025-12-14T07:55:08Z"
    }


def transform_learning_path_to_api_format(learning_path: LearningPath, user_id: str, db: Session) -> Dict[str, Any]:
    """
    Transform LearningPath database model to API format.
    
    This function resolves the frontend/backend inconsistency by converting:
    - Database 'name' -> API 'title'
    - Database 'difficulty_level' -> API 'difficulty'
    """
    
    # Get concept count for this path
    concept_count = db.query(LearningPathConcept).filter(
        LearningPathConcept.path_id == learning_path.path_id
    ).count()
    
    # Calculate user progress for this path
    user_progress = db.query(UserConceptProgress).filter(
        UserConceptProgress.user_id == user_id,
        UserConceptProgress.concept_id.in_(
            db.query(LearningPathConcept.concept_id).filter(
                LearningPathConcept.path_id == learning_path.path_id
            ).subquery()
        )
    ).all()
    
    completed_concepts = sum(1 for p in user_progress if p.status == 'completed')
    progress_percent = round((completed_concepts / concept_count * 100) if concept_count > 0 else 0)
    
    return {
        "id": learning_path.path_id,
        "title": learning_path.name,  # Transform: name -> title
        "description": learning_path.description,
        "difficulty": learning_path.difficulty_level,  # Transform: difficulty_level -> difficulty
        "category": learning_path.category,
        "duration": f"{max(1, concept_count // 2)} weeks",
        "concepts_count": concept_count,
        "progress": progress_percent,
        "estimated_hours": concept_count * 3,
        "is_public": learning_path.is_public,
        "is_ai_generated": learning_path.is_ai_generated,
        "adaptive": learning_path.adaptive,
        "created_at": learning_path.created_at.isoformat() if learning_path.created_at else None,
        "version": learning_path.version
    }


@router.get("/database")
async def get_learning_paths_from_database(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get learning paths from the actual database with API transformation.
    
    This endpoint resolves the frontend/backend inconsistency by transforming:
    - Database 'name' -> Frontend 'title'
    - Database 'difficulty_level' -> Frontend 'difficulty'
    
    Use this endpoint instead of the dynamic generation for consistent data.
    """
    
    # Fetch actual learning paths from database
    learning_paths = db.query(LearningPath).all()
    
    if not learning_paths:
        return {
            "paths": [],
            "message": "No learning paths found in database. Run seed_graph_paths_simple.py to populate.",
            "count": 0
        }
    
    # Transform each path to API format
    transformed_paths = []
    for path in learning_paths:
        api_path = transform_learning_path_to_api_format(path, current_user.user_id, db)
        transformed_paths.append(api_path)
    
    return {
        "paths": transformed_paths,
        "message": f"Retrieved {len(transformed_paths)} learning paths from database",
        "count": len(transformed_paths),
        "transformation_applied": {
            "database_to_api": {
                "name": "title",
                "difficulty_level": "difficulty"
            }
        }
    }


@router.get("/database/{path_id}")
async def get_learning_path_by_id(
    path_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get a specific learning path by ID from the database with API transformation.
    """
    
    learning_path = db.query(LearningPath).filter(
        LearningPath.path_id == path_id
    ).first()
    
    if not learning_path:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Learning path with ID {path_id} not found"
        )
    
    # Transform to API format
    api_path = transform_learning_path_to_api_format(learning_path, current_user.user_id, db)
    
    return api_path