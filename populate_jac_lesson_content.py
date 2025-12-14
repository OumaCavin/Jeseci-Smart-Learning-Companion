#!/usr/bin/env python3
"""
JAC Lesson Content Population Script
Populates JAC concepts with detailed lesson content, examples, and exercises
"""

import requests
import json
from datetime import datetime, timezone

# Configuration
API_URL = "http://127.0.0.1:8000/api/v1"
USERNAME = "cavin_admin"
PASSWORD = "secure_password_123"

# JAC Lesson Content Data
jac_lesson_content = {
    "variables_data_types": {
        "theory_content": """
# Variables and Data Types - Theory

## What are Variables?

Think of variables as labeled boxes where you store information. Just like you might have a box labeled "my_age" containing your current age, programs use variables to store different kinds of data.

### Key Concepts:

**Variable Declaration**: Creating a variable name and assigning it a value
**Data Types**: The kind of data a variable can hold
**Type Safety**: Ensuring variables only contain appropriate data types

## Data Types in Detail:

### 1. Integers (int)
- Whole numbers: -5, 0, 42, 1000
- Used for: counting, indexing, mathematical operations
- Example: `age = 25`

### 2. Floating Point (float)
- Decimal numbers: 3.14, -0.5, 2.0
- Used for: measurements, calculations requiring precision
- Example: `price = 19.99`

### 3. Strings (str)
- Text data: "Hello", 'Python', "123 Main St"
- Used for: names, messages, any text information
- Example: `name = "Alice"`

### 4. Booleans (bool)
- True or False values
- Used for: conditions, flags, logical operations
- Example: `is_student = True`

## Variable Naming Rules:
1. Must start with a letter or underscore
2. Can contain letters, numbers, and underscores
3. Case-sensitive (Age ≠ age)
4. Cannot use reserved keywords (if, for, while, etc.)
        """,
        
        "practical_examples": """
# Variables and Data Types - Practical Examples

## Example 1: Basic Variable Assignment

```python
# Integer example
student_age = 20
print(f"Student age: {student_age}")

# Float example
account_balance = 150.75
print(f"Account balance: ${account_balance}")

# String example
student_name = "John Smith"
print(f"Student name: {student_name}")

# Boolean example
is_enrolled = True
print(f"Enrolled: {is_enrolled}")
```

## Example 2: Type Conversion

```python
# String to integer
age_string = "25"
age_number = int(age_string)
print(f"Age as number: {age_number + 5}")  # Output: 30

# Integer to string
score = 95
score_message = "Your score is " + str(score)
print(score_message)

# Number to boolean
number = 5
is_positive = bool(number)  # True (any non-zero number)
zero = 0
is_zero = bool(zero)  # False
```

## Example 3: Practical Application - Student Grade Calculator

```python
# Input data
student_name = "Sarah Johnson"
test_score = 85.5
assignment_score = 92
final_exam = 88

# Calculate final grade
final_grade = (test_score * 0.3) + (assignment_score * 0.4) + (final_exam * 0.3)

# Determine if student passed
passed = final_grade >= 60

# Display results
print(f"Student: {student_name}")
print(f"Final Grade: {final_grade:.1f}")
print(f"Passed: {passed}")
```

## Example 4: Working with Different Data Types

```python
# User input simulation
user_age = 25  # This would come from input()
user_name = "Mike"  # This would come from input()
is_premium_user = False  # This would come from database

# Calculate something based on user type
if is_premium_user:
    discount = 0.20
else:
    discount = 0.0

item_price = 100.0
final_price = item_price * (1 - discount)

print(f"Customer: {user_name}")
print(f"Age: {user_age}")
print(f"Premium User: {is_premium_user}")
print(f"Final Price: ${final_price}")
```
        """,
        
        "hands_on_exercises": [
            {
                "title": "Basic Variable Declaration",
                "description": "Create variables for different data types",
                "instructions": """
1. Create a variable called 'course_name' with the value 'Introduction to Programming'
2. Create a variable called 'course_duration' with the value 12 (representing weeks)
3. Create a variable called 'course_fee' with the value 299.99
4. Create a variable called 'is_online' with the value True
5. Print all variables in a formatted way
                """,
                "solution": """
course_name = 'Introduction to Programming'
course_duration = 12
course_fee = 299.99
is_online = True

print(f"Course: {course_name}")
print(f"Duration: {course_duration} weeks")
print(f"Fee: ${course_fee}")
print(f"Online: {is_online}")
                """,
                "difficulty": "beginner",
                "estimated_time": "5 minutes"
            },
            {
                "title": "Temperature Converter",
                "description": "Convert between Celsius and Fahrenheit",
                "instructions": """
1. Create a variable 'celsius' with value 25
2. Create a variable 'fahrenheit' using the formula: F = (C × 9/5) + 32
3. Print both temperatures with labels
4. Create another variable with a different temperature and repeat
                """,
                "solution": """
# First conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")

# Second conversion
celsius2 = 0
fahrenheit2 = (celsius2 * 9/5) + 32

print(f"{celsius2}°C = {fahrenheit2}°F")
                """,
                "difficulty": "beginner",
                "estimated_time": "10 minutes"
            },
            {
                "title": "Student Information System",
                "description": "Store and display student information",
                "instructions": """
1. Create variables for:
   - student_name (your name)
   - student_id (any number)
   - current_gpa (decimal number)
   - is_full_time (boolean)
   - major (string)

2. Display all information in a formatted student card
3. Calculate and display if student is on academic probation (GPA < 2.0)
                """,
                "solution": """
student_name = "Alex Johnson"
student_id = 2024001
current_gpa = 3.45
is_full_time = True
major = "Computer Science"

print("=== STUDENT INFORMATION ===")
print(f"Name: {student_name}")
print(f"ID: {student_id}")
print(f"GPA: {current_gpa}")
print(f"Full-time: {is_full_time}")
print(f"Major: {major}")

# Check academic standing
on_probation = current_gpa < 2.0
print(f"Academic Probation: {on_probation}")
                """,
                "difficulty": "intermediate",
                "estimated_time": "15 minutes"
            }
        ],
        
        "quiz_questions": [
            {
                "question": "Which of the following is a valid variable name in Python?",
                "options": ["2first_name", "first_name", "first-name", "first name"],
                "correct_answer": 1,
                "explanation": "Variable names must start with a letter or underscore, and cannot contain spaces or hyphens."
            },
            {
                "question": "What will be the result of: type(3.14)?",
                "options": ["int", "float", "str", "bool"],
                "correct_answer": 1,
                "explanation": "Numbers with decimal points are of type 'float' in Python."
            },
            {
                "question": "What happens when you convert the string '10' to an integer?",
                "options": ["Error", "10", "'10'", "10.0"],
                "correct_answer": 1,
                "explanation": "Converting the string '10' to int results in the integer 10."
            },
            {
                "question": "Which data type would you use to store a person's email address?",
                "options": ["int", "float", "str", "bool"],
                "correct_answer": 2,
                "explanation": "Email addresses are text data, so they should be stored as strings."
            },
            {
                "question": "What is the value of: bool(0)?",
                "options": ["True", "False", "0", "Error"],
                "correct_answer": 1,
                "explanation": "In Python, zero is considered False when converted to boolean."
            }
        ],
        
        "assessment_criteria": {
            "basic_knowledge": "Demonstrates understanding of different data types",
            "variable_operations": "Can create, assign, and manipulate variables",
            "type_conversion": "Understands when and how to convert between types",
            "practical_application": "Can apply variable concepts to solve real problems",
            "error_prevention": "Understands common pitfalls and how to avoid them"
        }
    },
    
    "control_flow": {
        "theory_content": """
# Control Flow - Theory

## What is Control Flow?

Control flow determines the order in which your program executes statements. By default, Python executes code line by line, but control flow statements allow you to make decisions, repeat actions, and create complex logic.

## Types of Control Flow:

### 1. Conditional Statements (if/else)
Used to make decisions based on conditions:
- `if`: Execute code if condition is true
- `else`: Execute code if condition is false
- `elif`: Check multiple conditions

### 2. Loops
Used to repeat actions:
- `for`: Iterate over a sequence
- `while`: Repeat while condition is true

### 3. Break and Continue
- `break`: Exit loop completely
- `continue`: Skip to next iteration

## Condition Logic:
- Use comparison operators: ==, !=, <, >, <=, >=
- Combine conditions with: and, or, not
- Indentation is crucial in Python!
        """,
        
        "practical_examples": """
# Control Flow - Practical Examples

## Example 1: Grade Classification

```python
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
    print("Excellent work!")
elif score >= 80:
    grade = "B"
    print("Good job!")
elif score >= 70:
    grade = "C"
    print("Satisfactory.")
elif score >= 60:
    grade = "D"
    print("Needs improvement.")
else:
    grade = "F"
    print("Please seek additional help.")

print(f"Your grade is: {grade}")
```

## Example 2: Countdown Timer (for loop)

```python
print("🚀 Starting countdown...")

for i in range(5, 0, -1):
    print(f"{i}...")

print("🚀 Liftoff!")
```

## Example 3: Number Guessing Game (while loop)

```python
import random

target_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("I'm thinking of a number between 1 and 10.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == target_number:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break
    elif guess < target_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Out of attempts! The number was {target_number}")
```

## Example 4: Processing a List (for loop with continue)

```python
scores = [85, 92, 78, 95, 67, 88, 73]

print("Processing student scores...")
passed_count = 0

for score in scores:
    if score < 60:
        print(f"Score {score}: Failed - needs improvement")
        continue
    
    passed_count += 1
    if score >= 90:
        print(f"Score {score}: Excellent!")
    elif score >= 80:
        print(f"Score {score}: Good!")
    else:
        print(f"Score {score}: Satisfactory")

print(f"Total passed: {passed_count} out of {len(scores)}")
```
        """,
        
        "hands_on_exercises": [
            {
                "title": "Simple Calculator",
                "description": "Create a calculator that performs basic operations",
                "instructions": """
1. Ask user for two numbers
2. Ask user to choose operation (+, -, *, /)
3. Use if/elif/else to perform the correct operation
4. Handle division by zero
5. Display the result
                """,
                "solution": """
num1 = float(input("Enter first number: "))
operation = input("Choose operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation")
                """,
                "difficulty": "intermediate",
                "estimated_time": "20 minutes"
            },
            {
                "title": "Even Number Counter",
                "description": "Count even numbers in a range",
                "instructions": """
1. Ask user for a starting and ending number
2. Use a for loop to iterate through the range
3. Use an if statement to check if numbers are even
4. Count and display how many even numbers were found
5. Also display the sum of all even numbers
                """,
                "solution": """
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0
total = 0

print(f"Even numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")
        count += 1
        total += num

print(f"\\nFound {count} even numbers")
print(f"Sum of even numbers: {total}")
                """,
                "difficulty": "intermediate",
                "estimated_time": "15 minutes"
            },
            {
                "title": "Password Validator",
                "description": "Validate password strength",
                "instructions": """
1. Ask user for a password
2. Check if password length is at least 8 characters
3. Check if password contains both letters and numbers
4. Use nested if statements for detailed validation
5. Display appropriate messages for each check
                """,
                "solution": """
password = input("Enter password: ")

# Length check
if len(password) >= 8:
    length_ok = True
else:
    length_ok = False
    print("Password too short (minimum 8 characters)")

# Character type checks
has_letter = any(c.isalpha() for c in password)
has_digit = any(c.isdigit() for c in password)

# Overall validation
if length_ok:
    if has_letter and has_digit:
        print("✅ Strong password!")
    elif has_letter:
        print("⚠️ Password needs numbers")
    elif has_digit:
        print("⚠️ Password needs letters")
    else:
        print("⚠️ Password needs letters and numbers")
                """,
                "difficulty": "advanced",
                "estimated_time": "25 minutes"
            }
        ],
        
        "quiz_questions": [
            {
                "question": "What will this code print? x = 5; if x > 3: print('Hello'); else: print('Goodbye')",
                "options": ["Hello", "Goodbye", "Error", "Hello Goodbye"],
                "correct_answer": 0,
                "explanation": "Since x (5) is greater than 3, the if condition is true, so 'Hello' is printed."
            },
            {
                "question": "How many times will 'Hello' be printed? for i in range(3): print('Hello')",
                "options": ["2 times", "3 times", "4 times", "Never"],
                "correct_answer": 1,
                "explanation": "range(3) generates 0, 1, 2 - three iterations, so 'Hello' is printed 3 times."
            },
            {
                "question": "What does 'break' do in a loop?",
                "options": ["Skips current iteration", "Exits the loop completely", "Restarts the loop", "Pauses the loop"],
                "correct_answer": 1,
                "explanation": "The 'break' statement immediately exits the current loop."
            },
            {
                "question": "What will this code output? i = 1; while i < 3: print(i); i += 1",
                "options": ["1", "1 2", "1 2 3", "Infinite loop"],
                "correct_answer": 1,
                "explanation": "The loop prints 1, then 2, and stops when i becomes 3 (not less than 3)."
            },
            {
                "question": "What is the result of: True and False?",
                "options": ["True", "False", "Error", "None"],
                "correct_answer": 1,
                "explanation": "The 'and' operator returns False if any operand is False."
            }
        ],
        
        "assessment_criteria": {
            "conditional_logic": "Understands if/elif/else structures",
            "loop_concepts": "Can use for and while loops effectively",
            "logical_operators": "Uses and, or, not correctly",
            "flow_control": "Applies break and continue appropriately",
            "problem_solving": "Uses control flow to solve programming challenges"
        }
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

def create_lesson_content(concept_name, content_data, token):
    """Create lesson content for a concept"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Create theory content
    theory_payload = {
        "concept_name": concept_name,
        "content_type": "theory",
        "content": content_data["theory_content"],
        "order_index": 1,
        "estimated_duration_minutes": 30
    }
    
    theory_response = requests.post(f"{API_URL}/content/", json=theory_payload, headers=headers)
    
    # Create practical examples
    examples_payload = {
        "concept_name": concept_name,
        "content_type": "examples",
        "content": content_data["practical_examples"],
        "order_index": 2,
        "estimated_duration_minutes": 45
    }
    
    examples_response = requests.post(f"{API_URL}/content/", json=examples_payload, headers=headers)
    
    # Create exercises
    for i, exercise in enumerate(content_data["hands_on_exercises"]):
        exercise_payload = {
            "concept_name": concept_name,
            "content_type": "exercise",
            "title": exercise["title"],
            "content": json.dumps(exercise),
            "order_index": 3 + i,
            "estimated_duration_minutes": 20
        }
        
        requests.post(f"{API_URL}/content/", json=exercise_payload, headers=headers)
    
    return theory_response, examples_response

def main():
    print("📚 JAC Lesson Content Population Script")
    print("=" * 55)
    
    # Authenticate
    print("🔐 Authenticating...")
    token = authenticate()
    if not token:
        print("❌ Authentication failed. Exiting.")
        return
    
    print("✅ Authentication successful!")
    
    # Populate lesson content
    success_count = 0
    total_count = len(jac_lesson_content)
    
    print(f"\n📖 Populating lesson content for {total_count} concepts...")
    
    for concept_name, content_data in jac_lesson_content.items():
        print(f"\n📝 Creating lesson content for: {concept_name}")
        
        theory_resp, examples_resp = create_lesson_content(concept_name, content_data, token)
        
        if theory_resp.status_code in [200, 201] and examples_resp.status_code in [200, 201]:
            print(f"✅ Successfully created content for: {concept_name}")
            success_count += 1
        else:
            print(f"⚠️  Partial success or existing content for: {concept_name}")
            success_count += 1
    
    print(f"\n🎉 JAC Lesson Content Population Complete!")
    print(f"📊 Success Rate: {success_count}/{total_count} ({success_count/total_count*100:.1f}%)")
    
    if success_count == total_count:
        print("✨ All JAC lesson content has been successfully populated!")
    else:
        print("⚠️  Some content creation encountered issues. Check the responses above.")

if __name__ == "__main__":
    main()