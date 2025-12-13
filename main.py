"""
Main FastAPI application for Jeseci Smart Learning Companion
Database-powered API with PostgreSQL, Redis, and Neo4j support
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn
import os
from dotenv import load_dotenv

from config.database import (
    init_db, close_db_connections, check_all_connections,
    get_db, get_redis_connection, get_neo4j_driver
)
from api.v1 import (
    auth, users, concepts, learning_paths, progress, 
    quizzes, achievements, analytics
)


# Load environment variables
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    print("🚀 Starting Jeseci Smart Learning Companion API...")
    
    # Initialize database
    init_db()
    
    # Check connections
    connections = check_all_connections()
    print(f"📊 Database connections: {connections}")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down Jeseci API...")
    close_db_connections()


# Create FastAPI application
app = FastAPI(
    title="Jeseci Smart Learning Companion API",
    description="AI-powered personalized learning platform with knowledge graph and adaptive learning paths",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs" if os.getenv("DEBUG", "false").lower() == "true" else None,
    redoc_url="/redoc" if os.getenv("DEBUG", "false").lower() == "true" else None
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").replace(" ", "").replace('"', '').split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"] if os.getenv("DEBUG", "false").lower() == "true" else ["localhost", "127.0.0.1"]
)


# Include API routers
api_prefix = os.getenv("API_V1_STR", "/api/v1")

app.include_router(
    auth.router,
    prefix=f"{api_prefix}/auth",
    tags=["Authentication"]
)

app.include_router(
    users.router,
    prefix=f"{api_prefix}/users",
    tags=["Users"]
)

app.include_router(
    concepts.router,
    prefix=f"{api_prefix}/concepts",
    tags=["Concepts"]
)

app.include_router(
    learning_paths.router,
    prefix=f"{api_prefix}/learning-paths",
    tags=["Learning Paths"]
)

app.include_router(
    progress.router,
    prefix=f"{api_prefix}/progress",
    tags=["Progress"]
)

app.include_router(
    quizzes.router,
    prefix=f"{api_prefix}/quizzes",
    tags=["Quizzes"]
)

app.include_router(
    achievements.router,
    prefix=f"{api_prefix}/achievements",
    tags=["Achievements"]
)

app.include_router(
    analytics.router,
    prefix=f"{api_prefix}/analytics",
    tags=["Analytics"]
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Jeseci Smart Learning Companion API",
        "version": "1.0.0",
        "docs": "/docs" if os.getenv("DEBUG", "false").lower() == "true" else "disabled",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    connections = check_all_connections()
    all_healthy = all(connections.values())
    
    return {
        "status": "healthy" if all_healthy else "unhealthy",
        "database_connections": connections,
        "timestamp": "2025-12-09T22:55:08Z"
    }


@app.get("/info")
async def api_info():
    """API information endpoint"""
    return {
        "api_name": "Jeseci Smart Learning Companion",
        "version": "1.0.0",
        "description": "AI-powered personalized learning platform",
        "features": [
            "User Management and Authentication",
            "Knowledge Graph and Concept Modeling", 
            "Adaptive Learning Paths",
            "Progress Tracking and Analytics",
            "AI-powered Quiz Generation",
            "Achievement System",
            "Real-time Analytics"
        ],
        "supported_databases": [
            "PostgreSQL (Primary)",
            "SQLite (Development)",
            "Redis (Caching)",
            "Neo4j (Graph Database)"
        ],
        "endpoints": {
            "authentication": f"{api_prefix}/auth",
            "users": f"{api_prefix}/users",
            "concepts": f"{api_prefix}/concepts",
            "learning_paths": f"{api_prefix}/learning-paths",
            "progress": f"{api_prefix}/progress",
            "quizzes": f"{api_prefix}/quizzes",
            "achievements": f"{api_prefix}/achievements",
            "analytics": f"{api_prefix}/analytics"
        }
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=os.getenv("DEBUG", "false").lower() == "true",
        log_level=os.getenv("LOG_LEVEL", "info").lower()
    )