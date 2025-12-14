#!/usr/bin/env python3
"""
JAC (Jeseci Academic Curriculum) Concepts Seeding Script
Populates the database with structured academic programming concepts
"""

import requests
import json
from datetime import datetime

# Configuration
API_URL = "http://127.0.0.1:8000/api/v1"
USERNAME = "cavin_admin"
PASSWORD = "secure_password_123"

# JAC Academic Curriculum Data
jac_concepts_data = {
    "variables_data_types": {
        "name": "variables_data_types",
        "display_name": "Variables and Data Types",
        "description": "Understanding how to store and manipulate different types of data in programming languages.",
        "detailed_description": "Variables are containers that store data values, while data types define the kind of data a variable can hold. This fundamental concept forms the building blocks of all programming languages and is essential for writing any meaningful program.",
        "category": "Programming Fundamentals",
        "subcategory": "Basic Concepts",
        "domain": "Computer Science",
        "difficulty_level": "beginner",
        "complexity_score": 3.5,
        "cognitive_load": 3.2,
        "key_terms": ["variable", "data type", "integer", "float", "string", "boolean", "type casting", "declaration", "assignment", "scope"],
        "synonyms": ["Variables", "Data Types", "Variable Declaration"],
        "learning_objectives": [
            "Understand what variables are and how they work",
            "Learn different data types (int, float, string, boolean)",
            "Practice variable declaration and assignment",
            "Understand type casting and conversion",
            "Learn about variable scope and lifetime"
        ],
        "practical_applications": [
            "Storing user input",
            "Calculating mathematical operations",
            "Managing program state",
            "Data processing",
            "Game development"
        ],
        "real_world_examples": [
            "Calculator applications storing numbers",
            "User registration forms storing profile data",
            "Shopping carts storing product information",
            "Temperature conversion tools",
            "Score tracking in games"
        ],
        "common_misconceptions": [
            "Variables are the same as values",
            "All data types work the same way",
            "Variable names don't matter",
            "Scope doesn't affect functionality",
            "Type casting always works safely"
        ],
        "prerequisites": ["none"],
        "learning_path": "programming_fundamentals",
        "estimated_duration_hours": 4,
        "prerequisite_score": 0.0,
        "follow_up_concepts": ["control_flow", "functions", "operators"]
    },
    
    "control_flow": {
        "name": "control_flow",
        "display_name": "Control Flow",
        "description": "Learning how to control the execution flow of programs using conditionals, loops, and branching statements.",
        "detailed_description": "Control flow mechanisms allow programmers to control the order in which code executes. This includes conditional statements (if/else), loops (for, while), and branching logic that enables programs to make decisions and repeat actions.",
        "category": "Programming Fundamentals",
        "subcategory": "Logic and Control",
        "domain": "Computer Science",
        "difficulty_level": "beginner",
        "complexity_score": 4.2,
        "cognitive_load": 4.5,
        "key_terms": ["if statement", "else", "elif", "for loop", "while loop", "break", "continue", "switch case", "nested loops", "condition"],
        "synonyms": ["Conditionals", "Loops", "Decision Making"],
        "learning_objectives": [
            "Master conditional statements (if/else)",
            "Understand loop structures (for, while)",
            "Learn to use break and continue statements",
            "Practice nested control structures",
            "Apply logical operators effectively"
        ],
        "practical_applications": [
            "User authentication systems",
            "Game logic and rules",
            "Data validation",
            "Menu-driven programs",
            "Search algorithms"
        ],
        "real_world_examples": [
            "Login systems checking credentials",
            "Recommendation engines",
            "Traffic light control systems",
            "Automated testing frameworks",
            "Game AI decision making"
        ],
        "common_misconceptions": [
            "Loops always need to run a fixed number of times",
            "Break and continue are the same",
            "Nested loops are always bad",
            "Conditionals are only for boolean logic",
            "Control flow doesn't affect performance"
        ],
        "prerequisites": ["variables_data_types"],
        "learning_path": "programming_fundamentals",
        "estimated_duration_hours": 6,
        "prerequisite_score": 3.5,
        "follow_up_concepts": ["functions", "arrays_lists", "error_handling"]
    },
    
    "functions": {
        "name": "functions",
        "display_name": "Functions",
        "description": "Understanding how to create reusable code blocks that perform specific tasks and can be called multiple times.",
        "detailed_description": "Functions are self-contained blocks of code that perform a specific task. They allow programmers to write reusable code, avoid repetition, organize code logically, and make programs more maintainable and readable.",
        "category": "Programming Fundamentals",
        "subcategory": "Code Organization",
        "domain": "Computer Science",
        "difficulty_level": "intermediate",
        "complexity_score": 5.8,
        "cognitive_load": 6.2,
        "key_terms": ["function", "parameter", "argument", "return value", "scope", "recursion", "function call", "function definition", "local variable", "global variable"],
        "synonyms": ["Methods", "Procedures", "Subroutines"],
        "learning_objectives": [
            "Understand function syntax and structure",
            "Master parameter passing and return values",
            "Learn about function scope and variable visibility",
            "Practice writing recursive functions",
            "Apply functions to solve complex problems"
        ],
        "practical_applications": [
            "Code reusability and modularity",
            "Mathematical calculations",
            "Data processing pipelines",
            "API design and implementation",
            "Algorithm implementations"
        ],
        "real_world_examples": [
            "Mathematical libraries (sin, cos, sqrt)",
            "String manipulation functions",
            "Database query functions",
            "File processing utilities",
            "Authentication and authorization functions"
        ],
        "common_misconceptions": [
            "Functions always need to return something",
            "More parameters always make functions better",
            "Global variables are always bad",
            "Recursion is only for mathematical problems",
            "Functions should always be short"
        ],
        "prerequisites": ["variables_data_types", "control_flow"],
        "learning_path": "programming_fundamentals",
        "estimated_duration_hours": 8,
        "prerequisite_score": 7.0,
        "follow_up_concepts": ["arrays_lists", "object_oriented", "algorithms"]
    },
    
    "arrays_lists": {
        "name": "arrays_lists",
        "display_name": "Arrays and Lists",
        "description": "Learning to work with collections of data using arrays, lists, and other data structures.",
        "detailed_description": "Arrays and lists are fundamental data structures that allow programmers to store and manipulate collections of data. They enable efficient organization, searching, and processing of multiple related data items.",
        "category": "Programming Fundamentals",
        "subcategory": "Data Structures",
        "domain": "Computer Science",
        "difficulty_level": "intermediate",
        "complexity_score": 6.5,
        "cognitive_load": 7.0,
        "key_terms": ["array", "list", "index", "element", "dimension", "multidimensional", "array length", "list comprehension", "iteration", "filter", "map"],
        "synonyms": ["Collections", "Sequences", "Data Containers"],
        "learning_objectives": [
            "Understand array and list basics",
            "Master indexing and element access",
            "Learn array/list manipulation methods",
            "Practice iteration over collections",
            "Apply lists to solve real-world problems"
        ],
        "practical_applications": [
            "Storing student grades",
            "Managing inventory systems",
            "Processing user input collections",
            "Database record management",
            "Game score tracking"
        ],
        "real_world_examples": [
            "Student grade management systems",
            "Shopping cart with multiple items",
            "Contact list applications",
            "Music playlist management",
            "Employee database systems"
        ],
        "common_misconceptions": [
            "Arrays and lists are always the same",
            "Indexing always starts at 1",
            "Arrays are always faster than lists",
            "All elements must be the same type",
            "Arrays have unlimited size"
        ],
        "prerequisites": ["variables_data_types", "functions"],
        "learning_path": "programming_fundamentals",
        "estimated_duration_hours": 7,
        "prerequisite_score": 10.0,
        "follow_up_concepts": ["object_oriented", "file_handling", "searching_sorting"]
    },
    
    "object_oriented": {
        "name": "object_oriented",
        "display_name": "Object-Oriented Programming",
        "description": "Understanding the principles of OOP including classes, objects, inheritance, and polymorphism.",
        "detailed_description": "Object-Oriented Programming is a programming paradigm that uses objects and classes to organize code. It promotes code reusability, maintainability, and scalability through concepts like encapsulation, inheritance, and polymorphism.",
        "category": "Programming Fundamentals",
        "subcategory": "Advanced Concepts",
        "domain": "Computer Science",
        "difficulty_level": "advanced",
        "complexity_score": 8.5,
        "cognitive_load": 9.0,
        "key_terms": ["class", "object", "inheritance", "polymorphism", "encapsulation", "abstraction", "method", "attribute", "constructor", "instance"],
        "synonyms": ["OOP", "Classes and Objects", "Object-Based Programming"],
        "learning_objectives": [
            "Understand classes and objects fundamentals",
            "Master inheritance and its types",
            "Learn encapsulation principles",
            "Practice polymorphism implementation",
            "Apply OOP principles to design systems"
        ],
        "practical_applications": [
            "GUI application development",
            "Game character systems",
            "Database modeling",
            "Software architecture design",
            "Library and framework development"
        ],
        "real_world_examples": [
            "Banking system with account classes",
            "E-commerce product management",
            "Social media user profiles",
            "Vehicle simulation games",
            "Employee management systems"
        ],
        "common_misconceptions": [
            "OOP is only for large projects",
            "Inheritance should be used everywhere",
            "Private methods can't be accessed",
            "All problems require OOP solutions",
            "More classes always mean better code"
        ],
        "prerequisites": ["functions", "arrays_lists"],
        "learning_path": "programming_fundamentals",
        "estimated_duration_hours": 12,
        "prerequisite_score": 13.0,
        "follow_up_concepts": ["design_patterns", "software_architecture", "databases"]
    },
    
    "error_handling": {
        "name": "error_handling",
        "display_name": "Error Handling and Debugging",
        "description": "Learning to handle exceptions, debug code, and write robust programs that handle edge cases.",
        "detailed_description": "Error handling and debugging are crucial skills for writing reliable software. This includes understanding different types of errors, implementing proper exception handling, using debugging tools, and writing code that gracefully handles unexpected situations.",
        "category": "Programming Fundamentals",
        "subcategory": "Robustness",
        "domain": "Computer Science",
        "difficulty_level": "intermediate",
        "complexity_score": 7.2,
        "cognitive_load": 7.8,
        "key_terms": ["exception", "try", "catch", "finally", "error", "debugging", "traceback", "stack trace", "logging", "validation"],
        "synonyms": ["Exception Handling", "Debugging", "Error Management"],
        "learning_objectives": [
            "Understand different types of errors",
            "Master try-catch-finally structures",
            "Learn debugging techniques and tools",
            "Practice input validation",
            "Implement proper error logging"
        ],
        "practical_applications": [
            "User input validation",
            "File operation safety",
            "Network communication robustness",
            "Database operation reliability",
            "Web application security"
        ],
        "real_world_examples": [
            "Login form error messages",
            "File upload validation",
            "Network timeout handling",
            "Database connection failures",
            "API error responses"
        ],
        "common_misconceptions": [
            "All errors should be caught",
            "Exception handling makes code slow",
            "Silent failures are acceptable",
            "Debugging is only for beginners",
            "Error messages should be technical"
        ],
        "prerequisites": ["functions", "control_flow"],
        "learning_path": "programming_fundamentals",
        "estimated_duration_hours": 8,
        "prerequisite_score": 10.0,
        "follow_up_concepts": ["testing", "software_engineering", "web_development"]
    }
}

def authenticate():
    """Authenticate with the API"""
    auth_data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    
    response = requests.post(f"{API_URL}/auth/login", json=auth_data)
    if response.status_code == 200:
        token_data = response.json()
        return token_data["access_token"]
    else:
        print(f"Authentication failed: {response.status_code}")
        return None

def create_concept(concept_data, token):
    """Create a single concept via API"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(f"{API_URL}/concepts/", json=concept_data, headers=headers)
    return response

def main():
    print("🎓 JAC Concepts Seeding Script")
    print("=" * 50)
    
    # Authenticate
    print("🔐 Authenticating...")
    token = authenticate()
    if not token:
        print("❌ Authentication failed. Exiting.")
        return
    
    print("✅ Authentication successful!")
    
    # Create concepts
    success_count = 0
    total_count = len(jac_concepts_data)
    
    print(f"\n📚 Seeding {total_count} JAC concepts...")
    
    for concept_name, concept_data in jac_concepts_data.items():
        print(f"\n📝 Creating concept: {concept_data['display_name']}")
        
        response = create_concept(concept_data, token)
        
        if response.status_code in [200, 201]:
            print(f"✅ Successfully created: {concept_data['display_name']}")
            success_count += 1
        elif response.status_code == 400:
            print(f"⚠️  Concept already exists: {concept_data['display_name']}")
            success_count += 1
        else:
            print(f"❌ Failed to create {concept_data['display_name']}: {response.status_code}")
            print(f"   Response: {response.text}")
    
    print(f"\n🎉 JAC Concepts Seeding Complete!")
    print(f"📊 Success Rate: {success_count}/{total_count} ({success_count/total_count*100:.1f}%)")
    
    if success_count == total_count:
        print("✨ All JAC concepts have been successfully seeded!")
    else:
        print("⚠️  Some concepts failed to seed. Check the errors above.")

if __name__ == "__main__":
    main()