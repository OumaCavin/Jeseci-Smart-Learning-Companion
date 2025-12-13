"""
Concepts API endpoints
Knowledge graph and concept management
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from pydantic import BaseModel

from api.v1.auth import get_current_user
from config.database import get_db
from database.models import Concept, UserProgress


# Pydantic models
class ConceptCreate(BaseModel):
    name: str
    display_name: str
    description: str
    detailed_description: Optional[str] = None
    category: str
    subcategory: Optional[str] = None
    domain: str
    difficulty_level: str
    complexity_score: Optional[float] = 0.0
    cognitive_load: Optional[float] = 0.0
    key_terms: Optional[List[str]] = []
    synonyms: Optional[List[str]] = []
    learning_objectives: Optional[List[str]] = []
    practical_applications: Optional[List[str]] = []
    real_world_examples: Optional[List[str]] = []
    common_misconceptions: Optional[List[str]] = []


class ConceptUpdate(BaseModel):
    display_name: Optional[str] = None
    description: Optional[str] = None
    detailed_description: Optional[str] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
    domain: Optional[str] = None
    difficulty_level: Optional[str] = None
    complexity_score: Optional[float] = None
    cognitive_load: Optional[float] = None
    key_terms: Optional[List[str]] = None
    synonyms: Optional[List[str]] = None
    learning_objectives: Optional[List[str]] = None
    practical_applications: Optional[List[str]] = None
    real_world_examples: Optional[List[str]] = None
    common_misconceptions: Optional[List[str]] = None


class ConceptResponse(BaseModel):
    concept_id: str
    name: str
    display_name: str
    description: str
    detailed_description: Optional[str]
    category: str
    subcategory: Optional[str]
    domain: str
    difficulty_level: str
    complexity_score: float
    cognitive_load: float
    key_terms: List[str]
    synonyms: List[str]
    learning_objectives: List[str]
    practical_applications: List[str]
    real_world_examples: List[str]
    common_misconceptions: List[str]
    mastery_score: float
    confidence_score: float
    usage_frequency: float
    success_rate: float
    engagement_score: float
    content_quality_score: float
    ai_generated_content: bool
    created_at: str
    updated_at: str


class ConceptSearch(BaseModel):
    query: Optional[str] = None
    category: Optional[str] = None
    domain: Optional[str] = None
    difficulty_level: Optional[str] = None
    limit: Optional[int] = 20
    offset: Optional[int] = 0


# Router instance
router = APIRouter()


@router.get("/", response_model=List[ConceptResponse])
async def get_concepts(
    search_params: ConceptSearch = Depends(),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get concepts with filtering and search"""
    
    query = db.query(Concept)
    
    # Apply filters
    if search_params.query:
        query = query.filter(
            or_(
                Concept.name.ilike(f"%{search_params.query}%"),
                Concept.display_name.ilike(f"%{search_params.query}%"),
                Concept.description.ilike(f"%{search_params.query}%"),
                Concept.key_terms.any(search_params.query)
            )
        )
    
    if search_params.category:
        query = query.filter(Concept.category == search_params.category)
    
    if search_params.domain:
        query = query.filter(Concept.domain == search_params.domain)
    
    if search_params.difficulty_level:
        query = query.filter(Concept.difficulty_level == search_params.difficulty_level)
    
    # Order by relevance and get results
    concepts = query.order_by(Concept.usage_frequency.desc()).offset(
        search_params.offset
    ).limit(search_params.limit).all()
    
    return [
        ConceptResponse(
            concept_id=str(concept.concept_id),
            name=concept.name,
            display_name=concept.display_name,
            description=concept.description,
            detailed_description=concept.detailed_description,
            category=concept.category,
            subcategory=concept.subcategory,
            domain=concept.domain,
            difficulty_level=concept.difficulty_level,
            complexity_score=concept.complexity_score,
            cognitive_load=concept.cognitive_load,
            key_terms=concept.key_terms,
            synonyms=concept.synonyms,
            learning_objectives=concept.learning_objectives,
            practical_applications=concept.practical_applications,
            real_world_examples=concept.real_world_examples,
            common_misconceptions=concept.common_misconceptions,
            mastery_score=concept.mastery_score,
            confidence_score=concept.confidence_score,
            usage_frequency=concept.usage_frequency,
            success_rate=concept.success_rate,
            engagement_score=concept.engagement_score,
            content_quality_score=concept.content_quality_score,
            ai_generated_content=concept.ai_generated_content,
            created_at=concept.created_at.isoformat(),
            updated_at=concept.updated_at.isoformat()
        )
        for concept in concepts
    ]


@router.get("/{concept_id}", response_model=ConceptResponse)
async def get_concept(
    concept_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific concept by ID"""
    
    concept = db.query(Concept).filter(Concept.concept_id == concept_id).first()
    
    if not concept:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Concept not found"
        )
    
    return ConceptResponse(
        concept_id=str(concept.concept_id),
        name=concept.name,
        display_name=concept.display_name,
        description=concept.description,
        detailed_description=concept.detailed_description,
        category=concept.category,
        subcategory=concept.subcategory,
        domain=concept.domain,
        difficulty_level=concept.difficulty_level,
        complexity_score=concept.complexity_score,
        cognitive_load=concept.cognitive_load,
        key_terms=concept.key_terms,
        synonyms=concept.synonyms,
        learning_objectives=concept.learning_objectives,
        practical_applications=concept.practical_applications,
        real_world_examples=concept.real_world_examples,
        common_misconceptions=concept.common_misconceptions,
        mastery_score=concept.mastery_score,
        confidence_score=concept.confidence_score,
        usage_frequency=concept.usage_frequency,
        success_rate=concept.success_rate,
        engagement_score=concept.engagement_score,
        content_quality_score=concept.content_quality_score,
        ai_generated_content=concept.ai_generated_content,
        created_at=concept.created_at.isoformat(),
        updated_at=concept.updated_at.isoformat()
    )


@router.post("/", response_model=ConceptResponse)
async def create_concept(
    concept_data: ConceptCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create new concept (admin/teachers only in production)"""
    
    # Check if concept with same name already exists
    existing_concept = db.query(Concept).filter(Concept.name == concept_data.name).first()
    
    if existing_concept:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Concept with this name already exists"
        )
    
    # Create new concept
    concept = Concept(
        name=concept_data.name,
        display_name=concept_data.display_name,
        description=concept_data.description,
        detailed_description=concept_data.detailed_description,
        category=concept_data.category,
        subcategory=concept_data.subcategory,
        domain=concept_data.domain,
        difficulty_level=concept_data.difficulty_level,
        complexity_score=concept_data.complexity_score,
        cognitive_load=concept_data.cognitive_load,
        key_terms=concept_data.key_terms,
        synonyms=concept_data.synonyms,
        learning_objectives=concept_data.learning_objectives,
        practical_applications=concept_data.practical_applications,
        real_world_examples=concept_data.real_world_examples,
        common_misconceptions=concept_data.common_misconceptions,
        ai_generated_content=False
    )
    
    db.add(concept)
    db.commit()
    db.refresh(concept)
    
    return ConceptResponse(
        concept_id=str(concept.concept_id),
        name=concept.name,
        display_name=concept.display_name,
        description=concept.description,
        detailed_description=concept.detailed_description,
        category=concept.category,
        subcategory=concept.subcategory,
        domain=concept.domain,
        difficulty_level=concept.difficulty_level,
        complexity_score=concept.complexity_score,
        cognitive_load=concept.cognitive_load,
        key_terms=concept.key_terms,
        synonyms=concept.synonyms,
        learning_objectives=concept.learning_objectives,
        practical_applications=concept.practical_applications,
        real_world_examples=concept.real_world_examples,
        common_misconceptions=concept.common_misconceptions,
        mastery_score=concept.mastery_score,
        confidence_score=concept.confidence_score,
        usage_frequency=concept.usage_frequency,
        success_rate=concept.success_rate,
        engagement_score=concept.engagement_score,
        content_quality_score=concept.content_quality_score,
        ai_generated_content=concept.ai_generated_content,
        created_at=concept.created_at.isoformat(),
        updated_at=concept.updated_at.isoformat()
    )


@router.put("/{concept_id}", response_model=ConceptResponse)
async def update_concept(
    concept_id: str,
    concept_update: ConceptUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update concept"""
    
    concept = db.query(Concept).filter(Concept.concept_id == concept_id).first()
    
    if not concept:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Concept not found"
        )
    
    # Update fields
    update_data = concept_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(concept, field, value)
    
    concept.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(concept)
    
    return ConceptResponse(
        concept_id=str(concept.concept_id),
        name=concept.name,
        display_name=concept.display_name,
        description=concept.description,
        detailed_description=concept.detailed_description,
        category=concept.category,
        subcategory=concept.subcategory,
        domain=concept.domain,
        difficulty_level=concept.difficulty_level,
        complexity_score=concept.complexity_score,
        cognitive_load=concept.cognitive_load,
        key_terms=concept.key_terms,
        synonyms=concept.synonyms,
        learning_objectives=concept.learning_objectives,
        practical_applications=concept.practical_applications,
        real_world_examples=concept.real_world_examples,
        common_misconceptions=concept.common_misconceptions,
        mastery_score=concept.mastery_score,
        confidence_score=concept.confidence_score,
        usage_frequency=concept.usage_frequency,
        success_rate=concept.success_rate,
        engagement_score=concept.engagement_score,
        content_quality_score=concept.content_quality_score,
        ai_generated_content=concept.ai_generated_content,
        created_at=concept.created_at.isoformat(),
        updated_at=concept.updated_at.isoformat()
    )


@router.get("/{concept_id}/related")
async def get_related_concepts(
    concept_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get concepts related to the given concept"""
    
    concept = db.query(Concept).filter(Concept.concept_id == concept_id).first()
    
    if not concept:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Concept not found"
        )
    
    # Get related concepts through the many-to-many relationship
    related_concepts = concept.prerequisite_concepts
    
    return [
        {
            "concept_id": str(related_concept.concept_id),
            "name": related_concept.name,
            "display_name": related_concept.display_name,
            "category": related_concept.category,
            "difficulty_level": related_concept.difficulty_level,
            "relationship_type": "related"
        }
        for related_concept in related_concepts
    ]


@router.get("/{concept_id}/prerequisites")
async def get_concept_prerequisites(
    concept_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get prerequisite concepts for the given concept"""
    
    concept = db.query(Concept).filter(Concept.concept_id == concept_id).first()
    
    if not concept:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Concept not found"
        )
    
    # Get prerequisite concepts
    prerequisites = concept.dependent_concepts
    
    return [
        {
            "concept_id": str(prereq.concept_id),
            "name": prereq.name,
            "display_name": prereq.display_name,
            "category": prereq.category,
            "difficulty_level": prereq.difficulty_level,
            "relationship_type": "prerequisite"
        }
        for prereq in prerequisites
    ]


@router.get("/{concept_id}/user-progress")
async def get_user_concept_progress(
    concept_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get current user's progress on specific concept"""
    
    progress = db.query(UserProgress).filter(
        and_(
            UserProgress.user_id == current_user.user_id,
            UserProgress.concept_id == concept_id
        )
    ).first()
    
    if not progress:
        return {
            "concept_id": concept_id,
            "mastery_level": 0.0,
            "confidence_level": 0.0,
            "time_spent": 0,
            "review_count": 0,
            "success_rate": 0.0,
            "has_progress": False
        }
    
    return {
        "concept_id": concept_id,
        "mastery_level": progress.mastery_level,
        "confidence_level": progress.confidence_level,
        "time_spent": progress.time_spent,
        "review_count": progress.review_count,
        "success_rate": progress.success_rate,
        "average_score": progress.average_score,
        "streak_count": progress.streak_count,
        "first_attempt": progress.first_attempt.isoformat(),
        "last_review": progress.last_review.isoformat(),
        "next_review_date": progress.next_review_date.isoformat() if progress.next_review_date else None,
        "has_progress": True
    }


@router.get("/domains/list")
async def get_available_domains(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get list of available concept domains"""
    
    domains = db.query(Concept.domain).distinct().all()
    
    return {
        "domains": [domain[0] for domain in domains]
    }


@router.get("/categories/list")
async def get_available_categories(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get list of available concept categories"""
    
    categories = db.query(Concept.category).distinct().all()
    
    return {
        "categories": [category[0] for category in categories]
    }