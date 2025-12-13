"""
Database models for the Jeseci Smart Learning Companion
SQLite-compatible models for development and testing
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from config.database import Base

# Import SQLite-compatible models
from .sqlite_models import *