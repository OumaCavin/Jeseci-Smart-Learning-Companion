"""
Learning paths API endpoints
Adaptive learning path management and recommendations
"""

from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from api.v1.auth import get_current_user
from config.database import get_db
from database.models import User, LearningPath, LearningSession, Concept, UserConceptProgress


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


@router.post("/recommendations")
async def get_learning_recommendations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get AI-powered learning recommendations"""
    
    # Get user's progress
    user_progress = db.query(UserConceptProgress).filter(
        UserConceptProgress.user_id == current_user.user_id
    ).all()
    
    # Get all concepts
    all_concepts = db.query(Concept).all()
    
    # Simple recommendation logic: suggest uncompleted concepts
    completed_concept_ids = {p.concept_id for p in user_progress if p.status == 'completed'}
    
    recommendations = []
    for concept in all_concepts:
        if concept.concept_id not in completed_concept_ids:
            recommendations.append({
                "concept_id": concept.concept_id,
                "name": concept.display_name,
                "category": concept.category,
                "difficulty": concept.difficulty_level,
                "reason": "Based on your learning progress"
            })
    
    return {
        "recommendations": recommendations[:5],  # Top 5 recommendations
        "message": "Personalized recommendations based on your progress"
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