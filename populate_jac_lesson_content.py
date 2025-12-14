#!/usr/bin/env python3
"""
JAC Programming Lesson Content Population Script
Populates the lesson_content column with rich tutorial content for each JAC programming concept
"""

import json
import os
from datetime import datetime
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from database.models.sqlite_models import Concept, LearningPath, LearningPathConcept

def populate_lesson_content(db: Session):
    """Populate JAC concepts with rich lesson content"""
    print("📚 Populating JAC Concepts with Rich Lesson Content...")
    
    # Check if concepts exist
    concepts = db.query(Concept).filter(Concept.category == "JAC Programming").all()
    if not concepts:
        print("❌ No JAC concepts found. Run seed_jac_concepts.py first!")
        return
    
    print(f"Found {len(concepts)} JAC concepts to populate with content")
    
    # Define rich lesson content for each concept
    lesson_contents = {
        "jac_programming_fundamentals": """
# JAC Programming Fundamentals

## What is JAC?

JAC (Java-like Architecture for Computation) is a revolutionary programming language that introduces **Object-Spatial Programming (OSP)** - a paradigm where computation moves to data instead of data moving to computation.

## Key Concepts

### Dual Programming Paradigm
JAC offers two complementary approaches:
1. **Traditional Programming**: Familiar sequential, procedural code
2. **Object-Spatial Programming**: Graph-based, distributed computation

### Object-Spatial Programming (OSP)
OSP is built on three fundamental concepts:
- **Nodes**: Stateful entities that hold data
- **Edges**: Typed relationships between nodes
- **Walkers**: Mobile computation that traverses graphs

## Why JAC?

### Traditional Programming Problems
- **Scalability**: Hard to scale from single-user to millions
- **Persistence**: Manual database integration required
- **Distribution**: Complex distributed system development
- **State Management**: Difficult to manage application state

### JAC Solutions
- **Scale-Agnostic**: Code works for 1 user or 1 million without changes
- **Automatic Persistence**: Data persists automatically
- **Natural Distribution**: Built for distributed applications
- **Spatial Computation**: Computation moves to data

## Development Environment Setup

### Installation
```bash
# Install JAC compiler
pip install jac-lang

# Create new JAC project
jac new my_jac_app
cd my_jac_app
```

### Basic Project Structure
```
my_jac_app/
├── main.jac          # Main application entry point
├── models/           # Object definitions
├── walkers/          # Walker implementations
└── utils/            # Utility functions
```

## Your First JAC Program

```jac
# Traditional programming approach
def main() -> int:
    name: str = "JAC Developer"
    age: int = 25
    
    print(f"Hello, {name}! You are {age} years old.")
    return 0

# Run the program
if __name__ == "__main__":
    result = main()
```

## Next Steps

In the next lesson, we'll explore JAC's type system and variable declarations.
""",

        "jac_variables_data_types": """
# JAC Variables and Data Types

## Type System Overview

JAC uses **strong typing** with explicit type annotations for all variables and collections. This ensures type safety and prevents runtime errors.

## Primitive Data Types

### String Type
```jac
name: str = "Alice Johnson"
message: str = "Welcome to JAC programming!"
multiline: str = \"\"\"This is a
multi-line
string.\"\"\"
```

### Numeric Types
```jac
# Integer
count: int = 42
negative: int = -17
large_number: int = 1_000_000

# Float
price: float = 19.99
temperature: float = -5.5
scientific: float = 1.5e-3
```

### Boolean Type
```jac
is_active: bool = True
has_permission: bool = False
is_empty: bool = len("") == 0
```

## Collection Types

### Lists
```jac
# Typed lists
names: list[str] = ["Alice", "Bob", "Charlie"]
scores: list[int] = [95, 87, 92, 88]
mixed: list = ["text", 42, True]  # Less common

# List operations
numbers: list[int] = []
numbers.append(1)
numbers.extend([2, 3, 4])
```

### Dictionaries
```jac
# Typed dictionaries
user: dict[str, str] = {
    "name": "Alice",
    "email": "alice@example.com"
}

config: dict[str, int] = {
    "port": 8080,
    "timeout": 30,
    "retries": 3
}
```

### Sets
```jac
# Unique collections
tags: set[str] = {"python", "programming", "tutorial"}
numbers: set[int] = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
```

### Tuples
```jac
# Immutable collections
coordinates: tuple[int, int] = (10, 20)
rgb_color: tuple[int, int, int] = (255, 128, 0)
person: tuple[str, int, str] = ("Alice", 25, "Engineer")
```

## Type Annotations Best Practices

### Always Specify Types
```jac
# Good - explicit typing
user_count: int = get_user_count()
messages: list[str] = process_messages()

# Avoid - implicit typing
user_count = get_user_count()  # Less clear
```

### Collection Type Annotations
```jac
# Always specify element types for collections
scores: list[int] = [95, 87, 92]      # Clear intent
users: dict[str, User] = {}           # Strong typing
valid_emails: set[str] = set()        # Initialize empty set
```

## String Formatting

### F-Strings
```jac
name: str = "Alice"
age: int = 25

# Basic f-string
greeting: str = f"Hello, {name}! You are {age} years old."

# Expressions in f-strings
message: str = f"Total: ${price * quantity:.2f}"
status: str = f"Progress: {completed}/{total} ({completed/total*100:.1f}%)"
```

### String Methods
```jac
text: str = "  JAC Programming  "

# Common string operations
cleaned: str = text.strip()           # "JAC Programming"
uppercase: str = text.upper()         # "  JAC PROGRAMMING  "
lowercase: str = text.lower()         # "  jac programming  "
replaced: str = text.replace("JAC", "Java")  # "  Java Programming  "
```

## Practice Exercises

### Exercise 1: Student Grade Calculator
```jac
def calculate_letter_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the function
student_scores: list[int] = [95, 87, 73, 58, 42]
for score in student_scores:
    letter = calculate_letter_grade(score)
    print(f"Score {score}: Grade {letter}")
```

### Exercise 2: User Profile
```jac
def create_user_profile(name: str, age: int, email: str) -> dict[str, str]:
    return {
        "name": name,
        "age": str(age),
        "email": email,
        "status": "active" if age >= 18 else "minor"
    }

# Create user profiles
profiles: list[dict[str, str]] = [
    create_user_profile("Alice", 25, "alice@example.com"),
    create_user_profile("Bob", 17, "bob@example.com"),
    create_user_profile("Charlie", 30, "charlie@example.com")
]

for profile in profiles:
    print(f"User: {profile}")
```

## Common Mistakes to Avoid

1. **Forgetting Type Annotations**
   ```jac
   # Bad
   name = "Alice"  # Type unclear
   
   # Good
   name: str = "Alice"
   ```

2. **Incorrect Collection Types**
   ```jac
   # Bad - unclear element types
   data: list = [1, "text", True]
   
   # Good - explicit types
   data: list[int] = [1, 2, 3]
   ```

3. **Mutable Default Arguments**
   ```jac
   # Bad
   def add_item(item: str, items: list[str] = []):
       items.append(item)
   
   # Good
   def add_item(item: str, items: list[str] = None):
       if items is None:
           items = []
       items.append(item)
   ```

## Next Steps

In the next lesson, we'll explore JAC's control flow structures including conditionals, loops, and pattern matching.
""",

        "jac_control_flow": """
# JAC Control Flow

## Conditional Statements

JAC uses curly braces `{}` for code blocks, similar to C-style languages.

### Basic If-Else
```jac
def check_temperature(temp: int) -> str:
    if temp > 30:
        return "Hot"
    elif temp > 20:
        return "Warm"
    elif temp > 10:
        return "Cool"
    else:
        return "Cold"

# Test the function
temperatures: list[int] = [35, 25, 15, 5]
for temp in temperatures:
    result = check_temperature(temp)
    print(f"Temperature {temp}°C: {result}")
```

### Nested Conditionals
```jac
def classify_number(num: int) -> str:
    if num > 0:
        if num > 100:
            return "Large Positive"
        else:
            return "Small Positive"
    elif num < 0:
        if num < -100:
            return "Large Negative"
        else:
            return "Small Negative"
    else:
        return "Zero"

# Test with various numbers
test_numbers: list[int] = [150, 25, -25, -150, 0]
for num in test_numbers:
    classification = classify_number(num)
    print(f"{num}: {classification}")
```

## Loops

### While Loops
```jac
# Basic while loop
def count_to_n(n: int) -> int:
    count: int = 0
    while count < n:
        print(f"Count: {count}")
        count = count + 1
    return count

# User input simulation
def simulate_user_input() -> str:
    attempts: int = 0
    max_attempts: int = 3
    
    while attempts < max_attempts:
        print(f"Attempt {attempts + 1}/{max_attempts}")
        # Simulate user input
        user_input: str = "correct" if attempts == 2 else "wrong"
        print(f"User entered: {user_input}")
        
        if user_input == "correct":
            return "Success!"
        attempts = attempts + 1
    
    return "Failed after maximum attempts"
```

### For Loops

#### Counting Loops
```jac
# Count from 0 to 4
for i: int in range(5):
    print(f"Count: {i}")

# Count from 2 to 7
for i: int in range(2, 8):
    print(f"Count: {i}")

# Count with step
for i: int in range(0, 10, 2):
    print(f"Even number: {i}")
```

#### Iterating Collections
```jac
# Iterate over list
names: list[str] = ["Alice", "Bob", "Charlie"]
for name: str in names:
    print(f"Hello, {name}!")

# Iterate over dictionary
user: dict[str, str] = {
    "name": "Alice",
    "email": "alice@example.com",
    "role": "Developer"
}

for key: str in user:
    value: str = user[key]
    print(f"{key}: {value}")

# Iterate over dictionary items
for key: str, value: str in user.items():
    print(f"{key}: {value}")
```

#### Enumerate with Index
```jac
# Get both index and value
programming_languages: list[str] = ["Python", "JAC", "JavaScript", "Go"]

for index: int, language: str in enumerate(programming_languages):
    print(f"{index + 1}. {language}")
```

## Break and Continue

### Break Statement
```jac
def find_first_negative(numbers: list[int]) -> int:
    for num: int in numbers:
        if num < 0:
            print(f"Found first negative number: {num}")
            break
        else:
            print(f"Checking {num}: positive")
    
    return -1  # No negative found

# Test the function
positive_list: list[int] = [1, 2, 3, 4, 5]
mixed_list: list[int] = [1, 2, -3, 4, 5]

find_first_negative(positive_list)
find_first_negative(mixed_list)
```

### Continue Statement
```jac
def process_scores(scores: list[int]) -> list[int]:
    valid_scores: list[int] = []
    
    for score: int in scores:
        if score < 0 or score > 100:
            print(f"Invalid score {score}, skipping...")
            continue
        
        print(f"Processing valid score: {score}")
        valid_scores.append(score)
    
    return valid_scores

# Test with mixed data
all_scores: list[int] = [95, -5, 87, 105, 73, 0, 88]
valid_scores = process_scores(all_scores)
print(f"Valid scores: {valid_scores}")
```

## Pattern Matching

JAC supports advanced pattern matching for complex conditional logic.

### Basic Pattern Matching
```jac
def handle_http_status(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK - Success"
        case 201:
            return "Created - Resource created"
        case 400:
            return "Bad Request - Invalid input"
        case 401:
            return "Unauthorized - Authentication required"
        case 403:
            return "Forbidden - Access denied"
        case 404:
            return "Not Found - Resource not found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown status code: {status_code}"

# Test different status codes
status_codes: list[int] = [200, 404, 500, 999]
for code: int in status_codes:
    message: str = handle_http_status(code)
    print(f"Status {code}: {message}")
```

### Pattern Matching with Guards
```jac
def classify_age(age: int) -> str:
    match age:
        case age if age < 13:
            return "Child"
        case age if age < 18:
            return "Teenager"
        case age if age < 65:
            return "Adult"
        case age:
            return "Senior"

# Pattern matching with multiple conditions
def process_shape(shape_type: str, sides: int) -> str:
    match shape_type, sides:
        case "triangle", 3:
            return "Equilateral triangle"
        case "square", 4:
            return "Perfect square"
        case "pentagon", 5:
            return "Regular pentagon"
        case _, sides if sides < 3:
            return "Invalid shape - too few sides"
        case _:
            return f"Unknown {sides}-sided shape"
```

## Practical Examples

### Game Score Calculator
```jac
def calculate_grade(percentage: float) -> tuple[str, float]:
    match percentage:
        case percentage if percentage >= 90:
            return ("A", 4.0)
        case percentage if percentage >= 80:
            return ("B", 3.0)
        case percentage if percentage >= 70:
            return ("C", 2.0)
        case percentage if percentage >= 60:
            return ("D", 1.0)
        case _:
            return ("F", 0.0)

# Calculate grades for students
students: dict[str, float] = {
    "Alice": 95.5,
    "Bob": 87.3,
    "Charlie": 73.1,
    "Diana": 58.7
}

for name: str, score: float in students.items():
    letter: str, gpa: float = calculate_grade(score)
    print(f"{name}: {score}% → {letter} (GPA: {gpa})")
```

### Shopping Cart Validation
```jac
def validate_cart_item(item: dict[str, str]) -> tuple[bool, str]:
    name: str = item.get("name", "")
    price: str = item.get("price", "")
    quantity: str = item.get("quantity", "")
    
    # Validate name
    if len(name) == 0:
        return (False, "Item name is required")
    
    # Validate price
    try:
        price_float: float = float(price)
        if price_float <= 0:
            return (False, "Price must be positive")
    except ValueError:
        return (False, "Invalid price format")
    
    # Validate quantity
    try:
        quantity_int: int = int(quantity)
        if quantity_int <= 0:
            return (False, "Quantity must be positive")
        if quantity_int > 100:
            return (False, "Quantity too large")
    except ValueError:
        return (False, "Invalid quantity format")
    
    return (True, "Valid item")

# Test cart validation
cart: list[dict[str, str]] = [
    {"name": "Laptop", "price": "999.99", "quantity": "1"},
    {"name": "", "price": "50.00", "quantity": "2"},
    {"name": "Mouse", "price": "invalid", "quantity": "1"},
    {"name": "Keyboard", "price": "75.00", "quantity": "150"}
]

for item: dict[str, str] in cart:
    is_valid: bool, message: str = validate_cart_item(item)
    status: str = "✓" if is_valid else "✗"
    print(f"{status} {item}: {message}")
```

## Common Pitfalls

### Off-by-One Errors
```jac
# Common mistake
for i: int in range(1, 10):  # 1 to 9, missing 10
    print(i)

# Correct
for i: int in range(10):     # 0 to 9
    print(i)

# Or
for i: int in range(1, 11):  # 1 to 10
    print(i)
```

### Infinite Loops
```jac
# Dangerous - infinite loop
count: int = 0
while count < 10:
    print(count)
    # Forgot to increment count!

# Safe - proper loop
count: int = 0
while count < 10:
    print(count)
    count = count + 1  # Important!
```

## Best Practices

1. **Use Meaningful Variable Names**
   ```jac
   # Bad
   for i in range(10):
       print(i)
   
   # Good
   for student_index in range(student_count):
       print(f"Student {student_index + 1}")
   ```

2. **Keep Loops Simple**
   ```jac
   # Bad - complex nested logic
   for user in users:
       if user.active:
           for post in user.posts:
               if post.published:
                   for comment in post.comments:
                       if comment.approved:
                           process_comment(comment)
   
   # Good - break into functions
   def process_approved_comments(user: User):
       for post in user.posts:
           if post.published:
               for comment in post.comments:
                   if comment.approved:
                       process_comment(comment)
   ```

3. **Use Pattern Matching for Complex Conditions**
   ```jac
   # Instead of deeply nested if-else
   def handle_user_action(action: str, user_role: str) -> str:
       match action, user_role:
           case "delete", "admin":
               return "Permission granted"
           case "delete", _:
               return "Permission denied"
           case "edit", "admin" | "editor":
               return "Permission granted"
           case "edit", _:
               return "Permission denied"
   ```

## Next Steps

In the next lesson, we'll explore JAC functions and how to create reusable code blocks.
""",

        "jac_functions": """
# JAC Functions

## What are Functions?

Functions are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and make programs more maintainable and readable.

## Function Syntax

### Basic Function Definition
```jac
def greet_user(name: str) -> str:
    \"\"\"Return a greeting message for the user.\"\"\"
    message: str = f"Hello, {name}! Welcome to JAC programming."
    return message

# Call the function
greeting = greet_user("Alice")
print(greeting)  # Output: Hello, Alice! Welcome to JAC programming.
```

### Function with Multiple Parameters
```jac
def calculate_area(length: float, width: float) -> float:
    \"\"\"Calculate the area of a rectangle.\"\"\"
    area: float = length * width
    return area

# Calculate area
room_area = calculate_area(12.5, 8.3)
print(f"Room area: {room_area} square meters")
```

## Function Components

### Function Signature
- **def**: Keyword to define a function
- **Function name**: Descriptive name following naming conventions
- **Parameters**: Input values in parentheses
- **Return type**: Type annotation after arrow (->)
- **Function body**: Code block in curly braces

### Documentation Strings (Docstrings)
```jac
def calculate_bmi(weight: float, height: float) -> float:
    \"\"\"
    Calculate Body Mass Index (BMI).
    
    Args:
        weight: Weight in kilograms
        height: Height in meters
    
    Returns:
        BMI value as a float
        
    Example:
        bmi = calculate_bmi(70, 1.75)
        print(f"BMI: {bmi}")
    \"\"\"
    if height <= 0:
        raise ValueError("Height must be positive")
    
    bmi: float = weight / (height * height)
    return bmi
```

## Parameters and Arguments

### Default Parameters
```jac
def create_user(username: str, email: str = "", is_active: bool = True) -> dict[str, str]:
    \"\"\"Create a user dictionary with optional parameters.\"\"\"
    user: dict[str, str] = {
        "username": username,
        "email": email if email else f"{username}@example.com",
        "status": "active" if is_active else "inactive",
        "created_at": "2024-01-01"
    }
    return user

# Using default parameters
user1 = create_user("alice")
user2 = create_user("bob", "bob@company.com")
user3 = create_user("charlie", is_active=False)
```

### Named Parameters
```jac
def configure_application(port: int, host: str = "localhost", debug: bool = False) -> dict[str, str]:
    \"\"\"Configure application settings.\"\"\"
    return {
        "port": port,
        "host": host,
        "debug": debug,
        "ssl": port == 443
    }

# Using named parameters
config1 = configure_application(8080, debug=True)
config2 = configure_application(host="0.0.0.0", port=3000)
config3 = configure_application(port=443, host="secure.example.com", debug=False)
```

## Return Values

### Single Return Value
```jac
def get_square(number: int) -> int:
    return number * number

result = get_square(5)  # 25
```

### Multiple Return Values (Tuples)
```jac
def divide_numbers(dividend: float, divisor: float) -> tuple[float, str]:
    \"\"\"Divide two numbers and return result with status.\"\"\"
    if divisor == 0:
        return (0.0, "Cannot divide by zero")
    
    result: float = dividend / divisor
    status: str = "Success"
    return (result, status)

# Use multiple return values
quotient, message = divide_numbers(10, 2)
print(f"{message}: {quotient}")

quotient, message = divide_numbers(10, 0)
print(f"{message}: {quotient}")
```

### Early Returns
```jac
def find_maximum(numbers: list[int]) -> int:
    \"\"\"Find the maximum number in a list.\"\"\"
    if len(numbers) == 0:
        return 0  # Early return for empty list
    
    if len(numbers) == 1:
        return numbers[0]  # Early return for single element
    
    max_num: int = numbers[0]
    for num: int in numbers[1:]:
        if num > max_num:
            max_num = num
    
    return max_num
```

## Function Types and Patterns

### Pure Functions
```jac
def add_numbers(a: int, b: int) -> int:
    \"\"\"Pure function - same input always gives same output.\"\"\"
    return a + b

# No side effects, deterministic
result1 = add_numbers(5, 3)  # Always 8
result2 = add_numbers(5, 3)  # Always 8
```

### Functions with Side Effects
```jac
# Global variable (generally avoid)
total_score: int = 0

def add_to_total(score: int) -> None:
    \"\"\"Function that modifies external state.\"\"\"
    global total_score
    total_score = total_score + score
    print(f"Added {score}. New total: {total_score}")

# Better approach - return new state
def add_to_score(score: int, current_total: int) -> int:
    \"\"\"Function that returns new state.\"\"\"
    new_total: int = current_total + score
    return new_total
```

### Higher-Order Functions
```jac
def apply_operation(numbers: list[int], operation: def(int) -> int) -> list[int]:
    \"\"\"Apply a function to each number in a list.\"\"\"
    result: list[int] = []
    for num: int in numbers:
        result.append(operation(num))
    return result

# Define operations
def square(x: int) -> int:
    return x * x

def double(x: int) -> int:
    return x * 2

# Use higher-order function
numbers: list[int] = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)      # [1, 4, 9, 16, 25]
doubled = apply_operation(numbers, double)      # [2, 4, 6, 8, 10]
```

## Advanced Function Patterns

### Recursive Functions
```jac
def factorial(n: int) -> int:
    \"\"\"Calculate factorial of a number recursively.\"\"\"
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Calculate factorials
for i: int in range(1, 6):
    result: int = factorial(i)
    print(f"{i}! = {result}")
```

### Generator Functions
```jac
def fibonacci_sequence(count: int) -> list[int]:
    \"\"\"Generate Fibonacci sequence.\"\"\"
    if count <= 0:
        return []
    if count == 1:
        return [0]
    if count == 2:
        return [0, 1]
    
    sequence: list[int] = [0, 1]
    for i: int in range(2, count):
        next_num: int = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence

# Generate Fibonacci sequence
fib_sequence = fibonacci_sequence(10)
print(f"Fibonacci: {fib_sequence}")
```

### Functions with Error Handling
```jac
def safe_divide(numerator: float, denominator: float) -> tuple[float, str]:
    \"\"\"Safely divide two numbers with error handling.\"\"\"
    try:
        if denominator == 0:
            return (0.0, "Error: Division by zero")
        
        result: float = numerator / denominator
        return (result, "Success")
    except Exception as e:
        return (0.0, f"Error: {str(e)}")

# Test safe division
test_cases: list[tuple[float, float]] = [
    (10, 2),
    (10, 0),
    (5.5, 2.2),
    (100, -5)
]

for num, denom in test_cases:
    result, message = safe_divide(num, denom)
    print(f"{num} / {denom} = {result} ({message})")
```

## Practical Examples

### Data Processing Functions
```jac
def process_student_data(students: list[dict[str, str]]) -> dict[str, float]:
    \"\"\"Process student data and return statistics.\"\"\"
    if len(students) == 0:
        return {"average_grade": 0.0, "pass_rate": 0.0}
    
    total_grade: float = 0.0
    passed_count: int = 0
    
    for student: dict[str, str] in students:
        try:
            grade: float = float(student["grade"])
            total_grade = total_grade + grade
            
            if grade >= 60:
                passed_count = passed_count + 1
        except (ValueError, KeyError):
            continue  # Skip invalid data
    
    average_grade: float = total_grade / len(students)
    pass_rate: float = (passed_count / len(students)) * 100
    
    return {
        "average_grade": round(average_grade, 2),
        "pass_rate": round(pass_rate, 1)
    }

# Test with sample data
students_data: list[dict[str, str]] = [
    {"name": "Alice", "grade": "95"},
    {"name": "Bob", "grade": "78"},
    {"name": "Charlie", "grade": "55"},
    {"name": "Diana", "grade": "82"}
]

stats = process_student_data(students_data)
print(f"Class Statistics: {stats}")
```

### Utility Functions
```jac
def format_currency(amount: float, currency: str = "USD") -> str:
    \"\"\"Format a number as currency.\"\"\"
    symbols: dict[str, str] = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥"
    }
    
    symbol: str = symbols.get(currency, currency)
    formatted: str = f"{symbol}{amount:,.2f}"
    return formatted

def validate_email(email: str) -> bool:
    \"\"\"Simple email validation.\"\"\"
    if "@" not in email:
        return False
    
    parts: list[str] = email.split("@")
    if len(parts) != 2:
        return False
    
    username, domain = parts
    return len(username) > 0 and len(domain) > 2

# Test utility functions
prices: list[float] = [19.99, 1500.00, 75.5]
for price in prices:
    print(f"Price: {format_currency(price)}")

emails: list[str] = ["user@example.com", "invalid", "test@domain"]
for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")
```

## Best Practices

### Function Design Principles

1. **Single Responsibility**: Each function should do one thing well
2. **Descriptive Names**: Use clear, descriptive function names
3. **Small Functions**: Keep functions short and focused
4. **Pure When Possible**: Prefer pure functions over those with side effects
5. **Proper Documentation**: Include docstrings for all public functions

### Parameter Guidelines
```jac
# Good - clear parameters
def calculate_circle_area(radius: float) -> float:
    return 3.14159 * radius * radius

# Bad - unclear what parameters do
def calc(r: float) -> float:
    return 3.14159 * r * r
```

### Error Handling
```jac
# Good - proper error handling
def parse_positive_integer(value: str) -> tuple[int, str]:
    try:
        number: int = int(value)
        if number <= 0:
            return (0, "Value must be positive")
        return (number, "Success")
    except ValueError:
        return (0, "Invalid integer format")

# Bad - no error handling
def parse_number(value: str) -> int:
    return int(value)  # Can crash with invalid input
```

## Common Mistakes to Avoid

1. **Forgetting Return Statements**
   ```jac
   # Bad
   def greet(name: str):
       message = f"Hello, {name}!"
       # Missing return statement
   
   # Good
   def greet(name: str) -> str:
       return f"Hello, {name}!"
   ```

2. **Modifying Parameters Unnecessarily**
   ```jac
   # Bad - modifying input list
   def add_item_buggy(item: str, items: list[str]):
       items.append(item)  # Side effect
   
   # Good - return new list
   def add_item_good(item: str, items: list[str]) -> list[str]:
       new_items = items.copy()
       new_items.append(item)
       return new_items
   ```

3. **Complex Parameter Lists**
   ```jac
   # Bad - too many parameters
   def create_user_complex(name: str, email: str, age: int, city: str, country: str, is_active: bool) -> dict:
       # ...
   
   # Good - use configuration objects
   def create_user_good(config: dict[str, str]) -> dict:
       # ...
   ```

## Next Steps

In the next lesson, we'll explore JAC collections and data structures, learning how to work with lists, dictionaries, sets, and more advanced data organization techniques.
""",

        "jac_collections": """
# JAC Collections and Data Structures

## Overview of Collections

Collections are data structures that store multiple values. JAC provides several types of collections, each with specific characteristics and use cases.

## List Operations

### Creating and Initializing Lists
```jac
# Empty list
empty_list: list[int] = []

# List with initial values
numbers: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ["Alice", "Bob", "Charlie"]
mixed: list = [1, "hello", True, 3.14]

# List comprehension
squares: list[int] = [x * x for x in range(1, 6)]  # [1, 4, 9, 16, 25]
evens: list[int] = [x for x in range(1, 11) if x % 2 == 0]
```

### Adding and Removing Elements
```jac
# Adding elements
items: list[str] = []
items.append("first")      # ["first"]
items.extend(["second", "third"])  # ["first", "second", "third"]
items.insert(1, "inserted")  # ["first", "inserted", "second", "third"]

# Removing elements
items.remove("inserted")   # Removes first occurrence
popped: str = items.pop()  # Removes and returns last item
deleted: str = items.pop(0)  # Removes and returns first item

# Clearing list
items.clear()
```

### List Methods and Operations
```jac
# List methods
numbers: list[int] = [3, 1, 4, 1, 5, 9, 2, 6]

# Sorting
numbers.sort()             # [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Counting and finding
count_of_ones: int = numbers.count(1)  # 2
index_of_four: int = numbers.index(4)  # 3

# List operations
list1: list[int] = [1, 2, 3]
list2: list[int] = [4, 5, 6]
combined: list[int] = list1 + list2    # [1, 2, 3, 4, 5, 6]
repeated: list[str] = ["x"] * 3        # ["x", "x", "x"]
```

### Slicing Lists
```jac
fruits: list[str] = ["apple", "banana", "cherry", "date", "elderberry"]

# Basic slicing
first_three: list[str] = fruits[0:3]    # ["apple", "banana", "cherry"]
last_two: list[str] = fruits[-2:]       # ["date", "elderberry"]
middle: list[str] = fruits[1:4]         # ["banana", "cherry", "date"]

# Advanced slicing
every_other: list[str] = fruits[::2]     # ["apple", "cherry", "elderberry"]
reverse: list[str] = fruits[::-1]       # ["elderberry", "date", "cherry", "banana", "apple"]
```

## Dictionary Operations

### Creating and Accessing Dictionaries
```jac
# Empty dictionary
user_profile: dict[str, str] = {}

# Dictionary with initial values
user: dict[str, str] = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "role": "Developer"
}

# Accessing values
name: str = user["name"]                # "Alice Johnson"
role: str = user.get("role", "User")    # "Developer" (with default)

# Adding and updating
user["age"] = 25                        # Add new key-value pair
user.update({"city": "New York", "active": True})  # Update multiple values
```

### Dictionary Methods
```jac
user: dict[str, str] = {"name": "Alice", "email": "alice@example.com", "active": True}

# Getting keys, values, and items
keys: list[str] = list(user.keys())     # ["name", "email", "active"]
values: list = list(user.values())      # ["Alice", "alice@example.com", True]
items: list[tuple[str, str]] = list(user.items())  # [("name", "Alice"), ...]

# Dictionary methods
has_email: bool = "email" in user       # True
name_exists: bool = user.pop("name", None) is not None  # Remove and check

# Dictionary comprehensions
squared_numbers: dict[int, int] = {x: x*x for x in range(1, 6)}  # {1:1, 2:4, 3:9, 4:16, 5:25}
```

### Nested Dictionaries
```jac
# Complex nested structure
company: dict[str, str | dict] = {
    "name": "TechCorp",
    "founded": 2020,
    "location": {
        "city": "San Francisco",
        "state": "CA",
        "country": "USA"
    },
    "employees": {
        "Alice": {"role": "Engineer", "level": "Senior"},
        "Bob": {"role": "Designer", "level": "Junior"}
    }
}

# Accessing nested values
city: str = company["location"]["city"]  # "San Francisco"
alice_role: str = company["employees"]["Alice"]["role"]  # "Engineer"
```

## Set Operations

### Creating and Using Sets
```jac
# Creating sets
empty_set: set[int] = set()                    # Empty set (not {})
numbers_set: set[int] = {1, 2, 3, 4, 5}        # Set with values
from_list: set[str] = set(["apple", "banana"])  # Convert list to set

# Set operations
set1: set[int] = {1, 2, 3, 4}
set2: set[int] = {3, 4, 5, 6}

# Mathematical operations
union: set[int] = set1 | set2                  # {1, 2, 3, 4, 5, 6}
intersection: set[int] = set1 & set2           # {3, 4}
difference: set[int] = set1 - set2             # {1, 2}
symmetric_diff: set[int] = set1 ^ set2         # {1, 2, 5, 6}

# Set methods
set1.add(6)                                    # Add element
set1.remove(1)                                 # Remove element (raises error if not found)
set1.discard(1)                                # Remove element (no error if not found)
```

### Set Comprehensions and Use Cases
```jac
# Set comprehension
evens: set[int] = {x for x in range(1, 11) if x % 2 == 0}  # {2, 4, 6, 8, 10}

# Practical uses
# Remove duplicates from list
data: list[int] = [1, 2, 2, 3, 3, 3, 4, 5]
unique_data: list[int] = list(set(data))       # [1, 2, 3, 4, 5]

# Membership testing (very fast)
allowed_emails: set[str] = {"admin@example.com", "user@example.com"}
user_email: str = "user@example.com"
is_allowed: bool = user_email in allowed_emails  # True (O(1) lookup)
```

## Tuple Operations

### Creating and Using Tuples
```jac
# Creating tuples
empty_tuple: tuple = ()
single_item: tuple[int] = (42,)
coordinates: tuple[int, int] = (10, 20)
rgb_color: tuple[int, int, int] = (255, 128, 0)

# Tuple unpacking
x: int
y: int
x, y = coordinates                          # x = 10, y = 20

# Multiple assignment
name: str
age: int
city: str
name, age, city = ("Alice", 25, "New York")

# Tuple methods
numbers: tuple[int, ...] = (1, 2, 3, 2, 4, 2)
count_twos: int = numbers.count(2)         # 3
index_of_four: int = numbers.index(4)      # 4
```

## Collection Best Practices

### Type Annotations
```jac
# Always specify types for collections
names: list[str] = ["Alice", "Bob"]                    # List of strings
user_scores: dict[str, int] = {"Alice": 95, "Bob": 87}  # String to int mapping
unique_ids: set[int] = {1, 2, 3, 4, 5}                # Set of integers
coordinates: tuple[float, float] = (10.5, 20.3)        # Tuple of floats

# For complex nested structures
company_data: dict[str, str | int | list[str]] = {
    "name": "TechCorp",
    "employees": 150,
    "departments": ["Engineering", "Marketing", "Sales"]
}
```

### Performance Considerations
```jac
# Lists - good for ordered data, indexing
names: list[str] = ["Alice", "Bob", "Charlie"]
first_name: str = names[0]              # O(1) - very fast
last_name: str = names[-1]              # O(1) - very fast

# Sets - good for uniqueness and membership testing
allowed_users: set[str] = {"alice", "bob", "charlie"}
is_allowed: bool = "alice" in allowed_users  # O(1) - very fast

# Dictionaries - good for key-value lookups
user_scores: dict[str, int] = {"alice": 95, "bob": 87}
alice_score: int = user_scores["alice"]        # O(1) - very fast
```

### Common Patterns

#### Filtering Collections
```jac
# Filter list using list comprehension
scores: list[int] = [95, 87, 73, 58, 92, 45]
high_scores: list[int] = [score for score in scores if score >= 80]

# Filter dictionary
user_data: dict[str, int] = {"alice": 95, "bob": 87, "charlie": 73, "diana": 58}
passing_students: dict[str, int] = {name: score for name, score in user_data.items() if score >= 70}
```

#### Transforming Collections
```jac
# Map operation using list comprehension
names: list[str] = ["alice", "bob", "charlie"]
capitalized: list[str] = [name.title() for name in names]

# Transform dictionary values
user_scores: dict[str, int] = {"alice": 95, "bob": 87, "charlie": 73}
letter_grades: dict[str, str] = {name: "A" if score >= 90 else "B" if score >= 80 else "C" for name, score in user_scores.items()}
```

#### Grouping Data
```jac
# Grouping by using dictionaries
students: list[dict[str, str]] = [
    {"name": "Alice", "grade": "A", "subject": "Math"},
    {"name": "Bob", "grade": "B", "subject": "Math"},
    {"name": "Charlie", "grade": "A", "subject": "Science"},
    {"name": "Diana", "grade": "C", "subject": "Science"}
]

# Group by subject
by_subject: dict[str, list[dict]] = {}
for student in students:
    subject: str = student["subject"]
    if subject not in by_subject:
        by_subject[subject] = []
    by_subject[subject].append(student)
```

## Practical Examples

### Student Grade Management System
```jac
def create_gradebook() -> dict[str, list[dict]]:
    \"\"\"Create a student grade management system.\"\"\"
    gradebook: dict[str, list[dict]] = {}
    
    # Add students with multiple grades
    students: list[dict[str, str | list[int]]] = [
        {
            "name": "Alice Johnson",
            "id": "S001",
            "grades": [95, 87, 92, 88]
        },
        {
            "name": "Bob Smith",
            "id": "S002", 
            "grades": [78, 85, 79, 82]
        },
        {
            "name": "Charlie Brown",
            "id": "S003",
            "grades": [92, 96, 94, 98]
        }
    ]
    
    for student in students:
        name: str = student["name"]
        grades: list[int] = student["grades"]
        
        # Calculate statistics
        average: float = sum(grades) / len(grades)
        highest: int = max(grades)
        lowest: int = min(grades)
        
        # Determine letter grade
        if average >= 90:
            letter: str = "A"
        elif average >= 80:
            letter = "B"
        elif average >= 70:
            letter = "C"
        else:
            letter = "F"
        
        student_record: dict = {
            "name": name,
            "id": student["id"],
            "grades": grades,
            "average": round(average, 2),
            "highest": highest,
            "lowest": lowest,
            "letter_grade": letter
        }
        
        gradebook[name] = [student_record]
    
    return gradebook

# Test the gradebook system
book = create_gradebook()
for name, records in book.items():
    for record in records:
        print(f"{record['name']} ({record['id']}): Average {record['average']} ({record['letter_grade']})")
```

### Inventory Management
```jac
def manage_inventory() -> dict[str, dict]:
    \"\"\"Manage product inventory with categories.\"\"\"
    inventory: dict[str, dict] = {}
    
    # Product data
    products: list[dict] = [
        {
            "id": "P001",
            "name": "Laptop",
            "category": "Electronics",
            "price": 999.99,
            "stock": 15,
            "suppliers": ["TechCorp", "ElectroSupply"]
        },
        {
            "id": "P002",
            "name": "Office Chair",
            "category": "Furniture",
            "price": 199.99,
            "stock": 8,
            "suppliers": ["FurnitureCo"]
        },
        {
            "id": "P003",
            "name": "Monitor",
            "category": "Electronics", 
            "price": 299.99,
            "stock": 0,
            "suppliers": ["TechCorp", "DisplayPro"]
        }
    ]
    
    for product in products:
        product_id: str = product["id"]
        category: str = product["category"]
        
        # Add to inventory
        inventory[product_id] = product
        
        # Track categories
        if category not in inventory:
            inventory[category] = {"products": [], "total_value": 0.0}
        
        inventory[category]["products"].append(product_id)
        inventory[category]["total_value"] += product["price"] * product["stock"]
    
    return inventory

# Test inventory management
inv = manage_inventory()

# Show low stock items
print("Low Stock Alert:")
for product_id, product in inv.items():
    if isinstance(product, dict) and "stock" in product:
        if product["stock"] < 10:
            print(f"- {product['name']}: {product['stock']} units")

# Show category totals
print("\\nCategory Totals:")
for category, data in inv.items():
    if isinstance(data, dict) and "total_value" in data:
        print(f"- {category}: ${data['total_value']:.2f}")
```

### Social Network Friend System
```jac
def create_social_network() -> dict[str, set]:
    \"\"\"Create a simple social network with friend connections.\"\"\"
    network: dict[str, set] = {}
    
    # Friend connections (bidirectional)
    connections: list[tuple[str, str]] = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "Diana"),
        ("Charlie", "Diana"),
        ("Diana", "Eve")
    ]
    
    # Initialize user sets
    all_users: set[str] = set()
    for user1, user2 in connections:
        all_users.add(user1)
        all_users.add(user2)
    
    for user in all_users:
        network[user] = set()
    
    # Add connections
    for user1, user2 in connections:
        network[user1].add(user2)
        network[user2].add(user1)  # Bidirectional
    
    return network

def find_mutual_friends(network: dict[str, set], user1: str, user2: str) -> set:
    \"\"\"Find mutual friends between two users.\"\"\"
    if user1 not in network or user2 not in network:
        return set()
    
    friends1: set = network[user1]
    friends2: set = network[user2]
    return friends1 & friends2  # Intersection

def suggest_friends(network: dict[str, set], user: str) -> set:
    \"\"\"Suggest friends based on friend-of-friend logic.\"\"\"
    if user not in network:
        return set()
    
    friends: set = network[user]
    suggestions: set = set()
    
    for friend in friends:
        friend_of_friends: set = network[friend]
        # Add friends of friends (excluding self and existing friends)
        suggestions.update(friend_of_friends - friends - {user})
    
    return suggestions

# Test social network
network = create_social_network()

print("Social Network Connections:")
for user, friends in network.items():
    print(f"{user}: friends with {list(friends)}")

# Find mutual friends
mutual = find_mutual_friends(network, "Alice", "Diana")
print(f"\\nMutual friends between Alice and Diana: {list(mutual)}")

# Suggest friends
suggestions = suggest_friends(network, "Alice")
print(f"\\nFriend suggestions for Alice: {list(suggestions)}")
```

## Common Mistakes to Avoid

### 1. Modifying Collections While Iterating
```jac
# Bad - modifying list while iterating
numbers: list[int] = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Dangerous!

# Good - create new list
numbers: list[int] = [1, 2, 3, 4, 5]
even_numbers: list[int] = [num for num in numbers if num % 2 != 0]
```

### 2. Dictionary Key Errors
```jac
# Bad - accessing non-existent key
user: dict[str, str] = {"name": "Alice"}
age: int = user["age"]  # KeyError!

# Good - use get() method
age: int = user.get("age", 0)  # Returns 0 if key doesn't exist
```

### 3. Set vs Dictionary Confusion
```jac
# Bad - using {} for empty set
empty_set: set = {}  # This creates an empty dictionary!

# Good - use set() constructor
empty_set: set = set()

# Good - set with values
my_set: set = {1, 2, 3}  # This is correct
```

### 4. Mutable Default Arguments
```jac
# Bad - mutable default argument
def add_item(item: str, items: list[str] = []):
    items.append(item)

# Good - use None and create new list
def add_item(item: str, items: list[str] = None):
    if items is None:
        items = []
    items.append(item)
```

## Memory and Performance Tips

### Choose the Right Collection
- **List**: When order matters and you need indexing
- **Dictionary**: When you need key-value lookups
- **Set**: When you need to test membership or remove duplicates
- **Tuple**: When data shouldn't be modified

### Efficient Operations
```jac
# Use set for membership testing (O(1))
large_list: list[int] = list(range(1000000))
large_set: set[int] = set(large_list)

# Check membership
is_in_list: bool = 999999 in large_list      # O(n) - slow
is_in_set: bool = 999999 in large_set        # O(1) - fast

# Use dictionary for frequency counting
text: str = "hello world hello python world"
word_counts: dict[str, int = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
```

## Next Steps

In the next lesson, we'll explore JAC's Object-Oriented Programming features, learning how to create classes, objects, and implement the unique interface/implementation separation that JAC provides.
"""
    }
    
    # Update concepts with lesson content
    updated_count = 0
    for concept in concepts:
        concept_name = concept.name
        if concept_name in lesson_contents:
            # Set lesson content to the dedicated lesson_content column
            lesson_content = lesson_contents[concept_name]
            
            concept.lesson_content = lesson_content
            concept.updated_at = datetime.utcnow()
            
            updated_count += 1
            print(f"✅ Set lesson content for: {concept.display_name}")
        else:
            print(f"⚠️  No lesson content found for: {concept.display_name}")
    
    # Commit all changes
    db.commit()
    print(f"\n🎉 Successfully populated lesson content for {updated_count} concepts!")
    
    # Show summary
    print(f"📊 Summary:")
    print(f"   • Total JAC Concepts: {len(concepts)}")
    print(f"   • Concepts with Lesson Content: {updated_count}")
    print(f"   • Concepts missing content: {len(concepts) - updated_count}")

def main():
    """Main function to populate lesson content"""
    print("📚 Starting JAC Lesson Content Population...")
    
    # Create database session
    db = SessionLocal()
    
    try:
        populate_lesson_content(db)
        
        print("\n🎉 JAC Lesson Content population completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during lesson content population: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()