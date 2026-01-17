#!/usr/bin/env python3
"""
PCEP Python Exam Tutor - Interactive Certification Preparation
Comprehensive coverage of all PCEP exam topics with practice questions!
"""

import sys
import json
import os
import random


class PythonTutor:
    # Constants for duplicate literals
    OPTION_A_YES = "A) Yes"
    OPTION_B_NO = "B) No"
    OPTION_D_ERROR = "D) Error"
    PRESS_ENTER = "Press Enter to continue..."
    PRESS_ENTER_NEWLINE = "\nPress Enter to continue..."

    def __init__(self):  # NOSONAR - data initialization increases complexity
        self.progress_file = "pcep_tutor_progress.json"
        self.current_lesson = 0
        self.completed_lessons = set()
        self.quiz_scores = {}
        self.load_progress()
        
        self.lessons = [
            # SECTION 1: Introduction to Python and Computer Programming
            {
                "title": "Python Fundamentals & Compilation",
                "section": "PCEP Section 1",
                "content": """
PCEP EXAM TOPIC: Understanding Python basics, compilation vs interpretation

Python is an interpreted, high-level programming language created by Guido van Rossum.

Key Concepts for PCEP:
- Python is INTERPRETED (not compiled to machine code before running)
- CPython is the reference implementation (written in C)
- Python code is compiled to bytecode (.pyc files), then interpreted
- .pyc files are stored in __pycache__ directory
- Python is:
  * Multi-paradigm (procedural, OOP, functional)
  * Dynamically typed
  * Case-sensitive
  * Uses indentation for code blocks (usually 4 spaces)

Compilation vs Interpretation:
- Compiled: Source → Machine code → Execution (C, C++)
- Interpreted: Source → Executed line by line (Python, JavaScript)
- Python: Hybrid (source → bytecode → interpretation)
                """,
                "example": """
# Python basics - case sensitivity
Name = "Alice"
name = "Bob"
print(Name)  # Alice
print(name)  # Bob - different variable!

# Indentation is mandatory
if True:
    print("This is indented")  # 4 spaces
    print("This too")
# print("This would cause IndentationError if uncommented")

# Comments
# Single line comment
x = 5  # Inline comment
\"\"\"
Multi-line comment
or docstring
\"\"\"

# Python is dynamically typed
var = 10        # int
var = "hello"   # now it's str - no error!
print(var)
                """,
                "exercise": {
                    "description": "Create a variable 'python_version' and assign it the value 3. Then reassign it to 'PCEP'",
                    "hint": "python_version = 3, then python_version = 'PCEP'",
                    "check": lambda code: "python_version" in code and "=" in code
                },
                "quiz": [
                    {
                        "question": "Python is primarily a(n) _____ language.",
                        "options": ["A) Compiled", "B) Interpreted", "C) Assembly", "D) Machine"],
                        "answer": "B",
                        "explanation": "Python is an interpreted language. Code is executed by an interpreter."
                    },
                    {
                        "question": "What is stored in __pycache__ directory?",
                        "options": ["A) Source code", "B) Documentation", "C) Bytecode files (.pyc)", "D) Log files"],
                        "answer": "C",
                        "explanation": "Python compiles source code to bytecode (.pyc) files stored in __pycache__."
                    },
                    {
                        "question": "Is Python case-sensitive?",
                        "options": [PythonTutor.OPTION_A_YES, PythonTutor.OPTION_B_NO, "C) Only for variables", "D) Only for functions"],
                        "answer": "A",
                        "explanation": "Python is case-sensitive. 'Variable' and 'variable' are different identifiers."
                    }
                ]
            },
            # SECTION 2: Data Types, Variables, Basic I/O, Operators
            {
                "title": "Literals, Variables & Numeric Types",
                "section": "PCEP Section 2.1",
                "content": """
PCEP EXAM TOPIC: Literals, variables, and numeric data types

LITERALS - fixed values in code:
- Integer: 42, -10, 0
- Float: 3.14, -0.5, 4. (trailing dot is valid!)
- Scientific notation: 3e8 (3 × 10^8), 1.5e-3 (0.0015)
- Octal: 0o123 (prefix 0o)
- Hexadecimal: 0x1A (prefix 0x)
- String: "hello", 'world', '''multi
  line'''
- Boolean: True, False (capitalized!)
- None: represents absence of value

NUMERIC TYPES:
- int: unlimited precision (no overflow!)
- float: IEEE 754 double precision
- complex: 3+4j (j for imaginary part)

VARIABLES:
- Names: letters, digits, underscore (can't start with digit)
- Convention: lowercase_with_underscores (snake_case)
- Reserved keywords cannot be used as names
                """,
                "example": """
# Different number formats
decimal = 100
octal = 0o144       # 100 in octal
hexadecimal = 0x64  # 100 in hex
print(decimal, octal, hexadecimal)  # All print 100

# Floats
f1 = 3.14
f2 = 4.           # Valid! Same as 4.0
f3 = .5           # Same as 0.5
scientific = 3e2  # 300.0
print(f1, f2, f3, scientific)

# Underscores for readability (Python 3.6+)
million = 1_000_000
print(million)  # 1000000

# Multiple assignment
a = b = c = 0
x, y, z = 1, 2, 3
print(x, y, z)

# Type checking
print(type(42))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type(True))    # <class 'bool'>
                """,
                "exercise": {
                    "description": "Create an integer, float, and boolean variable. Use scientific notation for the float (e.g., 2e3)",
                    "hint": "num = 10, sci = 2e3, flag = True",
                    "check": lambda code: "=" in code and "e" in code.lower()
                },
                "quiz": [
                    {
                        "question": "What is the value of 0o12 in decimal?",
                        "options": ["A) 12", "B) 10", "C) 8", "D) 14"],
                        "answer": "B",
                        "explanation": "0o12 is octal. 1×8 + 2 = 10 in decimal."
                    },
                    {
                        "question": "Which is a valid float literal?",
                        "options": ["A) 4.", "B) 4,0", "C) 4f", "D) 4_f"],
                        "answer": "A",
                        "explanation": "4. is valid (equals 4.0). Python uses dots, not commas for decimals."
                    },
                    {
                        "question": "What does 2e3 equal?",
                        "options": ["A) 6", "B) 8", "C) 2000", "D) 23"],
                        "answer": "C",
                        "explanation": "2e3 means 2 × 10^3 = 2000"
                    }
                ]
            },
            {
                "title": "Operators & Expressions",
                "section": "PCEP Section 2.2",
                "content": """
PCEP EXAM TOPIC: Operators and their priorities

ARITHMETIC OPERATORS (highest to lowest priority):
1. ** (exponentiation) - right associative!
2. +x, -x (unary plus, minus)
3. *, /, //, % (multiply, divide, floor division, modulo)
4. +, - (addition, subtraction)

IMPORTANT:
- ** is right associative: 2**3**2 = 2**(3**2) = 512
- // is floor division: 7 // 2 = 3
- % is modulo (remainder): 7 % 3 = 1
- / always returns float: 6 / 3 = 2.0

SHORTCUT OPERATORS:
x += 1  # x = x + 1
x -= 2  # x = x - 2
x *= 3  # x = x * 3
x /= 4  # x = x / 4
x //= 5 # x = x // 5
x %= 6  # x = x % 6
x **= 2 # x = x ** 2

TYPE CONVERSIONS:
int(x), float(x), str(x)
                """,
                "example": """
# Operator priority
print(2 + 3 * 4)      # 14 (not 20)
print((2 + 3) * 4)    # 20
print(2 ** 3 ** 2)    # 512 (right associative!)
print((2 ** 3) ** 2)  # 64

# Division types
print(7 / 2)    # 3.5 (float division)
print(7 // 2)   # 3 (floor division)
print(7 % 2)    # 1 (remainder/modulo)
print(-7 // 2)  # -4 (floors toward negative infinity!)

# Unary operators
x = 5
print(+x)  # 5
print(-x)  # -5

# Shortcut operators
counter = 10
counter += 5  # Now 15
counter *= 2  # Now 30
print(counter)

# Type conversion
print(int(3.9))      # 3 (truncates)
print(int("42"))     # 42
print(float("3.14")) # 3.14
print(str(100))      # "100"
                """,
                "exercise": {
                    "description": "Calculate: 10 // 3 and 10 % 3. Store results in variables 'quotient' and 'remainder'",
                    "hint": "quotient = 10 // 3, remainder = 10 % 3",
                    "check": lambda code: "//" in code and "%" in code
                },
                "quiz": [
                    {
                        "question": "What is 2 ** 3 ** 2?",
                        "options": ["A) 64", "B) 512", "C) 256", "D) 128"],
                        "answer": "B",
                        "explanation": "** is right associative: 2**(3**2) = 2**9 = 512"
                    },
                    {
                        "question": "What is -11 // 2?",
                        "options": ["A) -5", "B) -5.5", "C) -6", "D) -4"],
                        "answer": "C",
                        "explanation": "Floor division floors toward negative infinity: -11 // 2 = -6"
                    },
                    {
                        "question": "What does x *= 3 mean?",
                        "options": ["A) x = 3", "B) x = x * 3", "C) x = x + 3", "D) x = 3 * x"],
                        "answer": "B",
                        "explanation": "x *= 3 is shorthand for x = x * 3"
                    }
                ]
            },
            {
                "title": "Strings & Basic I/O",
                "section": "PCEP Section 2.3",
                "content": """
PCEP EXAM TOPIC: String operations and input/output

STRINGS:
- Enclosed in quotes: "hello", 'world'
- Triple quotes for multiline: '''text''' or \"\"\"text\"\"\"
- Escape sequences: \\n (newline), \\t (tab), \\\\ (backslash), \\' \\"
- String concatenation: "hello" + " " + "world"
- String repetition: "Hi" * 3 = "HiHiHi"
- Indexing: s[0] (first char), s[-1] (last char)
- Slicing: s[start:end:step]
- Immutable: cannot change individual characters

STRING METHODS (important for PCEP):
- len(s): length
- s.upper(), s.lower(): case conversion
- s.strip(): remove whitespace from ends
- s.replace(old, new): replace substring
- s.split(): split into list
- s.find(sub): find substring (-1 if not found)
- s.isdigit(), s.isalpha(), s.isalnum(): check content

INPUT/OUTPUT:
- print(*values, sep=' ', end='\\n'): output
- input(prompt): read string from user (always returns string!)
                """,
                "example": """
# String basics
s = "Python"
print(s[0])      # P (first character)
print(s[-1])     # n (last character)
print(s[0:3])    # Pyt (slice: index 0, 1, 2)
print(s[::-1])   # nohtyP (reverse)

# String operations
print("Hello" + " " + "World")  # Concatenation
print("=" * 20)                 # Repetition

# Escape sequences
print("Line 1\\nLine 2")  # Newline
print("Column1\\tColumn2") # Tab

# String methods
text = "  Hello World  "
print(text.strip())       # "Hello World"
print(text.upper())       # "  HELLO WORLD  "
print(text.replace("World", "Python"))  # "  Hello Python  "

words = "apple,banana,cherry"
print(words.split(","))   # ['apple', 'banana', 'cherry']

# Type checking
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True

# Input (always returns string!)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))  # Convert to int

# Print with custom separator and end
print(1, 2, 3, sep="-")           # 1-2-3
print("Hello", end=" ")
print("World")                     # Hello World (no newline between)
                """,
                "exercise": {
                    "description": "Create a string 'pcep' and print it reversed and in uppercase",
                    "hint": "s = 'pcep', print(s[::-1].upper())",
                    "check": lambda code: "[::-1]" in code or ".upper()" in code.lower()
                },
                "quiz": [
                    {
                        "question": "What does 'Hi' * 3 produce?",
                        "options": ["A) HiHiHi", "B) Hi Hi Hi", "C) Hi3", PythonTutor.OPTION_D_ERROR],
                        "answer": "A",
                        "explanation": "String * number repeats the string that many times with no spaces."
                    },
                    {
                        "question": "What does input() return?",
                        "options": ["A) Integer", "B) Float", "C) String", "D) Depends on input"],
                        "answer": "C",
                        "explanation": "input() always returns a string, even if user enters numbers."
                    },
                    {
                        "question": "What is 'Python'[-1]?",
                        "options": ["A) P", "B) n", "C) o", PythonTutor.OPTION_D_ERROR],
                        "answer": "B",
                        "explanation": "Negative indices count from the end. -1 is the last character: 'n'"
                    }
                ]
            },
            # SECTION 3: Boolean, Control Flow, Lists, Logic
            {
                "title": "Boolean Values & Comparison Operators",
                "section": "PCEP Section 3.1",
                "content": """
PCEP EXAM TOPIC: Boolean values, relational operators, logic

BOOLEAN VALUES:
- True, False (must be capitalized!)
- Result of comparisons and logical operations

COMPARISON OPERATORS:
- == (equal to) - NOT = (which is assignment!)
- != (not equal to)
- > (greater than)
- < (less than)
- >= (greater than or equal)
- <= (less than or equal)

LOGICAL OPERATORS (priority: not > and > or):
- not: logical negation
- and: True if both True
- or: True if at least one True

SHORT-CIRCUIT EVALUATION:
- and: stops at first False
- or: stops at first True

TRUTHY/FALSY VALUES:
Falsy: False, 0, 0.0, "", [], {}, None
Truthy: Everything else
                """,
                "example": """
# Boolean basics
print(True)          # True
print(type(True))    # <class 'bool'>
print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False
print(bool("text"))  # True

# Comparison operators
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True
print(5 <= 5)   # True
print("a" < "b")  # True (lexicographic comparison)

# Logical operators
print(True and True)   # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Operator priority: not > and > or
print(True or True and False)  # True (and first, then or)
# Equivalent to: True or (True and False) = True or False = True

# Short-circuit evaluation
x = 10
print(x > 5 or x < 0)  # True (doesn't check x < 0)
print(x > 20 and print("Hi"))  # False (doesn't print)

# Chaining comparisons
x = 5
print(1 < x < 10)  # True (equivalent to: 1 < x and x < 10)
                """,
                "exercise": {
                    "description": "Create a boolean expression checking if a number is between 10 and 20 (inclusive)",
                    "hint": "result = 10 <= num <= 20",
                    "check": lambda code: "<=" in code and ("and" in code.lower() or code.count("<=") >= 2)
                },
                "quiz": [
                    {
                        "question": "What is the result of: True or True and False?",
                        "options": ["A) True", "B) False", "C) Error", "D) None"],
                        "answer": "A",
                        "explanation": "'and' has higher priority than 'or': True or (True and False) = True or False = True"
                    },
                    {
                        "question": "Which is falsy in Python?",
                        "options": ["A) []", "B) 'False'", "C) 1", "D) [0]"],
                        "answer": "A",
                        "explanation": "Empty list [] is falsy. String 'False' is truthy (non-empty string)."
                    },
                    {
                        "question": "What does 5 == 5.0 return?",
                        "options": ["A) True", "B) False", "C) Error", "D) 1"],
                        "answer": "A",
                        "explanation": "== compares values, not types. 5 and 5.0 have equal values."
                    }
                ]
            },
            {
                "title": "Conditional Statements (if/elif/else)",
                "section": "PCEP Section 3.2",
                "content": """
PCEP EXAM TOPIC: Conditional execution

SYNTAX:
if condition:
    # code block (must be indented!)
elif another_condition:
    # code block
else:
    # code block

IMPORTANT:
- Colon (:) is REQUIRED after conditions
- Indentation is MANDATORY (usually 4 spaces)
- elif (not "else if")
- Can have multiple elif blocks
- else is optional

CONDITIONAL EXPRESSION (ternary operator):
value_if_true if condition else value_if_false

Example: max_val = a if a > b else b
                """,
                "example": """
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-elif-else chain
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# Nested conditions
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")

# Conditional expression (ternary)
a, b = 5, 10
max_value = a if a > b else b
print(f"Max: {max_value}")  # Max: 10

# Multiple conditions
temperature = 75
is_sunny = True
if temperature > 70 and is_sunny:
    print("Great day for the beach!")

# Checking membership
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("We have apples!")
                """,
                "exercise": {
                    "description": "Write an if-elif-else chain that categorizes a number as positive, negative, or zero",
                    "hint": "if num > 0: ... elif num < 0: ... else: ...",
                    "check": lambda code: 'if' in code.lower() and 'elif' in code.lower() and 'else' in code.lower()
                },
                "quiz": [
                    {
                        "question": "What comes after 'if condition'?",
                        "options": ["A) Colon :", "B) Semicolon ;", "C) Brace {", "D) Nothing"],
                        "answer": "A",
                        "explanation": "In Python, if statements must end with a colon :"
                    },
                    {
                        "question": "What is 10 if 5 > 3 else 20?",
                        "options": ["A) 10", "B) 20", "C) True", PythonTutor.OPTION_D_ERROR],
                        "answer": "A",
                        "explanation": "Since 5 > 3 is True, it returns 10"
                    },
                    {
                        "question": "Which keyword is used for additional conditions?",
                        "options": ["A) elseif", "B) else if", "C) elif", "D) elsif"],
                        "answer": "C",
                        "explanation": "Python uses 'elif' (not 'elseif' or 'else if')"
                    }
                ]
            },
            {
                "title": "Loops: while and for",
                "section": "PCEP Section 3.3",
                "content": """
PCEP EXAM TOPIC: Iteration with loops

WHILE LOOP:
while condition:
    # code block
    # update condition!
else:  # optional
    # executes if loop completes normally (no break)

FOR LOOP:
for variable in sequence:
    # code block
else:  # optional
    # executes if loop completes normally

RANGE FUNCTION:
- range(stop): 0 to stop-1
- range(start, stop): start to stop-1
- range(start, stop, step): with custom step

LOOP CONTROL:
- break: exit loop immediately
- continue: skip rest of current iteration
- pass: do nothing (placeholder)

IMPORTANT: else clause runs only if loop completes without break!
                """,
                "example": """
# while loop
count = 0
while count < 5:
    print(count)
    count += 1
# Prints: 0, 1, 2, 3, 4

# while with else
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop completed")

# for loop with range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# for loop with sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# break statement
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue statement
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)  # 0, 1, 3, 4

# else with break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")  # Won't print (break was used)

# Nested loops
for i in range(3):
    for j in range(2):
        print(f"({i},{j})")
                """,
                "exercise": {
                    "description": "Write a for loop that prints even numbers from 0 to 10 using range",
                    "hint": "for i in range(0, 11, 2): print(i)",
                    "check": lambda code: 'for' in code.lower() and 'range' in code.lower()
                },
                "quiz": [
                    {
                        "question": "What does range(5) produce?",
                        "options": ["A) 1,2,3,4,5", "B) 0,1,2,3,4", "C) 0,1,2,3,4,5", "D) 1,2,3,4"],
                        "answer": "B",
                        "explanation": "range(5) generates numbers from 0 to 4 (5 is excluded)"
                    },
                    {
                        "question": "What does 'continue' do?",
                        "options": ["A) Exit loop", "B) Skip to next iteration", "C) Restart loop", "D) Pause loop"],
                        "answer": "B",
                        "explanation": "'continue' skips the rest of the current iteration and goes to the next one"
                    },
                    {
                        "question": "When does the 'else' clause of a loop execute?",
                        "options": ["A) Always", "B) If loop completes without break", "C) If break is used", "D) Never"],
                        "answer": "B",
                        "explanation": "Loop's 'else' executes only if loop completes normally (no break)"
                    }
                ]
            },
            {
                "title": "Lists and List Operations",
                "section": "PCEP Section 3.4",
                "content": """
PCEP EXAM TOPIC: Lists - creation, indexing, slicing, methods

LISTS:
- Ordered, mutable sequences
- Created with square brackets: [1, 2, 3]
- Can contain mixed types: [1, "hello", 3.14]
- Zero-indexed: list[0] is first element
- Negative indexing: list[-1] is last element

SLICING: list[start:end:step]
- list[1:4]: elements at index 1, 2, 3
- list[:3]: first 3 elements
- list[2:]: from index 2 to end
- list[::-1]: reverse list
- list[::2]: every 2nd element

LIST METHODS (important for PCEP):
- append(x): add x to end
- insert(i, x): add x at index i
- remove(x): remove first occurrence of x
- pop(i): remove and return element at index i (default: last)
- index(x): return index of first x
- count(x): count occurrences of x
- sort(): sort in place
- reverse(): reverse in place
- clear(): remove all elements

OPERATORS:
- len(list): get length
- x in list: check membership
- list1 + list2: concatenation
- list * n: repetition
                """,
                "example": """
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# Indexing
print(numbers[0])   # 1 (first)
print(numbers[-1])  # 5 (last)
print(numbers[2])   # 3

# Slicing
print(numbers[1:4])    # [2, 3, 4]
print(numbers[:3])     # [1, 2, 3]
print(numbers[2:])     # [3, 4, 5]
print(numbers[::-1])   # [5, 4, 3, 2, 1] (reverse)
print(numbers[::2])    # [1, 3, 5] (every 2nd)

# Modifying lists
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]

# List methods
fruits = ["apple", "banana"]
fruits.append("cherry")      # ["apple", "banana", "cherry"]
fruits.insert(0, "mango")    # ["mango", "apple", "banana", "cherry"]
fruits.remove("apple")       # ["mango", "banana", "cherry"]
last = fruits.pop()          # Returns "cherry", list is ["mango", "banana"]

print(len(fruits))           # 2
print("mango" in fruits)     # True

# List operations
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2     # [1, 2, 3, 4]
repeated = list1 * 3         # [1, 2, 1, 2, 1, 2]

# Sorting
nums = [3, 1, 4, 1, 5]
nums.sort()                  # [1, 1, 3, 4, 5]
nums.reverse()               # [5, 4, 3, 1, 1]

# List iteration
for item in fruits:
    print(item)
                """,
                "exercise": {
                    "description": "Create a list with 5 numbers, add a 6th using append, and print it reversed using slicing",
                    "hint": "nums = [1,2,3,4,5], nums.append(6), print(nums[::-1])",
                    "check": lambda code: "append" in code.lower() and "[::-1]" in code
                },
                "quiz": [
                    {
                        "question": "What is [1,2,3][1:3]?",
                        "options": ["A) [1,2]", "B) [2,3]", "C) [1,2,3]", "D) [3]"],
                        "answer": "B",
                        "explanation": "[1:3] gets elements at index 1 and 2: [2, 3]"
                    },
                    {
                        "question": "What does list.pop() return?",
                        "options": ["A) First element", "B) Last element", "C) Nothing", "D) The list"],
                        "answer": "B",
                        "explanation": "pop() without argument removes and returns the last element"
                    },
                    {
                        "question": "What is [1,2,3][::-1]?",
                        "options": ["A) [1,2,3]", "B) [3,2,1]", "C) [2,1,3]", PythonTutor.OPTION_D_ERROR],
                        "answer": "B",
                        "explanation": "[::-1] reverses the list: [3, 2, 1]"
                    }
                ]
            },
            {
                "title": "Logical & Bitwise Operations",
                "section": "PCEP Section 3.5",
                "content": """
PCEP EXAM TOPIC: Logical and bitwise operations

LOGICAL OPERATORS (work with boolean values):
- and: both must be True
- or: at least one must be True  
- not: negation

BITWISE OPERATORS (work with bits in integers):
- & (AND): 1 if both bits are 1
- | (OR): 1 if at least one bit is 1
- ^ (XOR): 1 if bits are different
- ~ (NOT): flip all bits (NOT x = -x-1)
- << (left shift): multiply by 2^n
- >> (right shift): divide by 2^n

EXAMPLES:
12 in binary: 1100
10 in binary: 1010

12 & 10 = 1000 = 8
12 | 10 = 1110 = 14
12 ^ 10 = 0110 = 6
~12 = -13
12 << 1 = 24 (multiply by 2)
12 >> 1 = 6 (divide by 2)

PRIORITY: ~ > << >> > & > ^ > |
                """,
                "example": """
# Logical operators
print(True and True)   # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Bitwise operators
a = 12  # 1100 in binary
b = 10  # 1010 in binary

print(a & b)   # 8  (1000 in binary)
print(a | b)   # 14 (1110 in binary)
print(a ^ b)   # 6  (0110 in binary)
print(~a)      # -13
print(a << 1)  # 24 (shift left = multiply by 2)
print(a >> 1)  # 6  (shift right = divide by 2)

# Practical use: checking if number is even
num = 42
if num & 1 == 0:
    print("Even")  # If last bit is 0, number is even

# Setting flags
FLAG_READ = 1   # 001
FLAG_WRITE = 2  # 010
FLAG_EXEC = 4   # 100

permissions = FLAG_READ | FLAG_WRITE  # 011 = 3
print(permissions & FLAG_READ)  # Non-zero, has read permission
print(permissions & FLAG_EXEC)  # 0, no execute permission

# XOR swap (clever trick)
x, y = 5, 10
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)  # 10, 5 (swapped without temp variable!)
                """,
                "exercise": {
                    "description": "Use bitwise AND to check if number 17 is odd (hint: check last bit)",
                    "hint": "result = 17 & 1 (if 1, it's odd)",
                    "check": lambda code: "&" in code and ("17" in code or "num" in code.lower())
                },
                "quiz": [
                    {
                        "question": "What is 5 & 3?",
                        "options": ["A) 1", "B) 7", "C) 5", "D) 3"],
                        "answer": "A",
                        "explanation": "5=101, 3=011, AND=001=1"
                    },
                    {
                        "question": "What is 8 << 2?",
                        "options": ["A) 16", "B) 4", "C) 32", "D) 2"],
                        "answer": "C",
                        "explanation": "<< 2 shifts left 2 positions = multiply by 4: 8 * 4 = 32"
                    },
                    {
                        "question": "What is ~0?",
                        "options": ["A) 0", "B) -1", "C) 1", PythonTutor.OPTION_D_ERROR],
                        "answer": "B",
                        "explanation": "~x equals -x-1, so ~0 = -0-1 = -1"
                    }
                ]
            },
            # SECTION 4: Functions, Tuples, Dictionaries
            {
                "title": "Functions - Defining & Calling",
                "section": "PCEP Section 4.1",
                "content": """
PCEP EXAM TOPIC: Functions, parameters, return values, scope

FUNCTION DEFINITION:
def function_name(parameters):
    \"\"\"Docstring (optional)\"\"\"
    # function body
    return value  # optional

KEY CONCEPTS:
- def keyword starts function definition
- Parameters are optional
- return is optional (returns None if omitted)
- Functions must be defined before calling
- Docstrings describe function purpose

PARAMETERS:
- Positional: def func(a, b): ...
- Default values: def func(a, b=10): ...
- Keyword arguments: func(a=5, b=10)
- *args: variable positional arguments (tuple)
- **kwargs: variable keyword arguments (dict)

SCOPE:
- Local: variables inside function
- Global: variables outside functions
- global keyword: modify global variable inside function

IMPORTANT: None is returned if no return statement
                """,
                "example": """
# Simple function
def greet():
    print("Hello!")

greet()  # Call function

# Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default exponent=2)
print(power(5, 3))   # 125

# Keyword arguments
def describe_person(name, age, city):
    print(f"{name}, {age}, from {city}")

describe_person(age=25, name="Alice", city="NYC")

# Return multiple values (actually a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 3, 9, 2])
print(minimum, maximum)  # 1 9

# Function returning None
def no_return():
    print("I don't return anything")

result = no_return()
print(result)  # None

# Scope example
x = 10  # Global

def modify():
    global x  # Access global x
    x = 20

modify()
print(x)  # 20

# Variable arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
                """,
                "exercise": {
                    "description": "Create a function 'rectangle_area' that takes width and height, returns their product",
                    "hint": "def rectangle_area(width, height): return width * height",
                    "check": lambda code: 'def' in code.lower() and 'return' in code.lower()
                },
                "quiz": [
                    {
                        "question": "What does a function return if there's no return statement?",
                        "options": ["A) 0", "B) None", "C) False", PythonTutor.OPTION_D_ERROR],
                        "answer": "B",
                        "explanation": "Functions without return statement return None"
                    },
                    {
                        "question": "What keyword is used to access global variable in function?",
                        "options": ["A) global", "B) nonlocal", "C) extern", "D) public"],
                        "answer": "A",
                        "explanation": "'global' keyword allows modifying global variables inside functions"
                    },
                    {
                        "question": "In def func(a, b=5):, what is b?",
                        "options": ["A) Required parameter", "B) Default parameter", "C) Keyword parameter", "D) Variable parameter"],
                        "answer": "B",
                        "explanation": "b=5 is a default parameter (optional, has default value)"
                    }
                ]
            },
            {
                "title": "Tuples - Immutable Sequences",
                "section": "PCEP Section 4.2",
                "content": """
PCEP EXAM TOPIC: Tuples and tuple operations

TUPLES:
- Ordered, IMMUTABLE sequences
- Created with parentheses: (1, 2, 3)
- Or without: 1, 2, 3
- Single element tuple: (1,) - comma is required!
- Empty tuple: ()
- Can contain mixed types

CHARACTERISTICS:
- Cannot be modified after creation
- Faster than lists
- Can be used as dictionary keys (lists cannot!)
- Indexing and slicing work like lists
- Can be unpacked: a, b, c = (1, 2, 3)

TUPLE OPERATIONS:
- len(tuple): get length
- x in tuple: check membership
- tuple1 + tuple2: concatenation
- tuple * n: repetition
- tuple.count(x): count occurrences
- tuple.index(x): find index

WHEN TO USE:
- Data that shouldn't change
- Return multiple values from function
- Dictionary keys
- Faster than lists for read-only data
                """,
                "example": """
# Creating tuples
coordinates = (10, 20)
rgb = (255, 128, 0)
single = (42,)  # Comma is required!
empty = ()

# Tuple without parentheses
point = 5, 10, 15
print(type(point))  # <class 'tuple'>

# Indexing and slicing
numbers = (1, 2, 3, 4, 5)
print(numbers[0])     # 1
print(numbers[-1])    # 5
print(numbers[1:4])   # (2, 3, 4)

# Tuples are immutable
# numbers[0] = 10  # TypeError!

# Tuple unpacking
x, y = (10, 20)
print(x, y)  # 10 20

# Multiple assignment
a, b, c = 1, 2, 3

# Swap values
a, b = b, a
print(a, b)  # 2 1

# Function returning tuple
def get_dimensions():
    return 1920, 1080  # Returns tuple

width, height = get_dimensions()

# Tuple operations
t1 = (1, 2)
t2 = (3, 4)
combined = t1 + t2        # (1, 2, 3, 4)
repeated = t1 * 3         # (1, 2, 1, 2, 1, 2)

# Tuple methods
nums = (1, 2, 2, 3, 2)
print(nums.count(2))      # 3
print(nums.index(3))      # 3

# Nested tuples
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix[1][0])       # 3

# Converting between list and tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
                """,
                "exercise": {
                    "description": "Create a tuple with 3 values and unpack it into three variables",
                    "hint": "coords = (10, 20, 30) then x, y, z = coords",
                    "check": lambda code: "," in code and "=" in code
                },
                "quiz": [
                    {
                        "question": "How do you create a single-element tuple?",
                        "options": ["A) (1)", "B) (1,)", "C) [1]", "D) 1,"],
                        "answer": "B",
                        "explanation": "(1,) creates a tuple. (1) is just 1 in parentheses. Comma is required!"
                    },
                    {
                        "question": "Can tuples be modified after creation?",
                        "options": [PythonTutor.OPTION_A_YES, PythonTutor.OPTION_B_NO, "C) Only if nested", "D) Only first element"],
                        "answer": "B",
                        "explanation": "Tuples are immutable - cannot be changed after creation"
                    },
                    {
                        "question": "What does a, b = b, a do?",
                        "options": ["A) Error", "B) Swaps a and b", "C) Sets both to b", "D) Creates tuple"],
                        "answer": "B",
                        "explanation": "Tuple unpacking allows swapping without temporary variable"
                    }
                ]
            },
            {
                "title": "Dictionaries - Key-Value Pairs",
                "section": "PCEP Section 4.3",
                "content": """
PCEP EXAM TOPIC: Dictionaries and dictionary methods

DICTIONARIES:
- Unordered collection of key-value pairs
- Created with curly braces: {"key": "value"}
- Keys must be immutable (strings, numbers, tuples)
- Keys must be unique
- Values can be any type
- Very fast lookups

ACCESSING VALUES:
- dict[key]: get value (KeyError if key doesn't exist!)
- dict.get(key, default): safe access (returns default if key missing)

DICTIONARY METHODS (important for PCEP):
- dict.keys(): get all keys
- dict.values(): get all values
- dict.items(): get key-value pairs
- dict.update(other): merge dictionaries
- dict.pop(key): remove and return value
- dict.clear(): remove all items
- key in dict: check if key exists

OPERATIONS:
- len(dict): number of items
- dict[key] = value: add/update
- del dict[key]: remove item
                """,
                "example": """
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

empty_dict = {}
also_empty = dict()

# Accessing values
print(person["name"])        # Alice
print(person.get("age"))     # 25
print(person.get("email", "N/A"))  # N/A (key doesn't exist)

# Adding/modifying
person["email"] = "alice@example.com"  # Add
person["age"] = 26                      # Modify

# Removing items
age = person.pop("age")      # Remove and return value
del person["city"]           # Delete key
# person.clear()             # Remove all items

# Checking membership
print("name" in person)      # True
print("age" in person)       # False (we removed it)

# Dictionary methods
person = {"name": "Alice", "age": 25, "city": "NYC"}

print(person.keys())         # dict_keys(['name', 'age', 'city'])
print(person.values())       # dict_values(['Alice', 25, 'NYC'])
print(person.items())        # dict_items([('name', 'Alice'), ...])

# Iterating
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Update dictionary
person.update({"job": "Developer", "age": 26})
print(person)

# Dictionary from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))  # {"a": 1, "b": 2, "c": 3}

# Nested dictionaries
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print(users["user1"]["name"])  # Alice

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
                """,
                "exercise": {
                    "description": "Create a dictionary 'student' with keys: name, grade, subject. Access grade using .get()",
                    "hint": "student = {'name': 'John', 'grade': 'A', 'subject': 'Math'}, student.get('grade')",
                    "check": lambda code: "{" in code and ":" in code and ".get" in code.lower()
                },
                "quiz": [
                    {
                        "question": "What happens if you access dict[key] and key doesn't exist?",
                        "options": ["A) Returns None", "B) Returns 0", "C) KeyError", "D) Returns ''"],
                        "answer": "C",
                        "explanation": "Accessing non-existent key with [] raises KeyError. Use .get() for safe access."
                    },
                    {
                        "question": "Can a list be a dictionary key?",
                        "options": [PythonTutor.OPTION_A_YES, PythonTutor.OPTION_B_NO, "C) Only empty lists", "D) Only if unique"],
                        "answer": "B",
                        "explanation": "Dictionary keys must be immutable. Lists are mutable, so cannot be keys."
                    },
                    {
                        "question": "What does dict.items() return?",
                        "options": ["A) Keys only", "B) Values only", "C) Key-value pairs", "D) Length"],
                        "answer": "C",
                        "explanation": "dict.items() returns key-value pairs as tuples"
                    }
                ]
            },
            # SECTION 5: Modules and Packages
            {
                "title": "Modules and Packages",
                "section": "PCEP Section 4.4",
                "content": """
PCEP EXAM TOPIC: Importing and using modules

MODULES:
- Python file (.py) containing functions, classes, variables
- Imported using 'import' statement
- Allows code reusability and organization

IMPORT SYNTAX:
1. import module_name
   - Use: module_name.function()
   
2. import module_name as alias
   - Use: alias.function()
   
3. from module_name import function
   - Use: function()
   
4. from module_name import *
   - Imports all (not recommended!)

STANDARD LIBRARY MODULES (important for PCEP):
- math: mathematical functions
- random: random number generation
- platform: platform information
- sys: system-specific parameters

MODULE ATTRIBUTES:
- __name__: module name ("__main__" if run directly)
- dir(module): list all names in module

IMPORTANT:
- Import statements usually at top of file
- Each module imported only once
- from module import * can cause name conflicts
                """,
                "example": """
# Import entire module
import math
print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.ceil(3.2))    # 4
print(math.floor(3.8))   # 3

# Import with alias
import random as rnd
print(rnd.randint(1, 10))      # Random number 1-10
print(rnd.choice(['a', 'b', 'c']))  # Random choice

# Import specific items
from math import pi, sqrt
print(pi)       # 3.141592653589793
print(sqrt(25)) # 5.0 (no math. prefix needed!)

# Platform module
import platform
print(platform.platform())  # Platform info
print(platform.python_version())  # Python version

# Random module functions
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)  # Shuffle in place
print(numbers)

print(random.random())   # Random float 0.0-1.0
print(random.uniform(1, 10))  # Random float 1.0-10.0

# Math module functions
import math
print(math.pow(2, 3))    # 8.0 (same as 2**3)
print(math.factorial(5)) # 120
print(math.sin(math.pi/2))  # 1.0
print(math.log(10))      # Natural log
print(math.log10(100))   # 2.0 (base 10)

# Dir function - see module contents
print(dir(math)[:5])  # First 5 names in math module

# __name__ attribute
print(__name__)  # __main__ if running this file directly

# Creating simple module (in separate file)
# mymodule.py:
# def greet(name):
#     return f"Hello, {name}!"
# PI = 3.14159

# Using it:
# import mymodule
# print(mymodule.greet("Alice"))
# print(mymodule.PI)
                """,
                "exercise": {
                    "description": "Import the math module and use sqrt to find the square root of 144",
                    "hint": "import math, then print(math.sqrt(144))",
                    "check": lambda code: "import" in code.lower() and "math" in code.lower()
                },
                "quiz": [
                    {
                        "question": "After 'from math import pi', how do you access pi?",
                        "options": ["A) math.pi", "B) pi", "C) import.pi", "D) from.pi"],
                        "answer": "B",
                        "explanation": "'from math import pi' imports pi directly, use it without prefix"
                    },
                    {
                        "question": "What is __name__ when file is run directly?",
                        "options": ["A) '__main__'", "B) filename", "C) '__file__'", "D) 'main'"],
                        "answer": "A",
                        "explanation": "__name__ is '__main__' when script is executed directly"
                    },
                    {
                        "question": "What does random.randint(1, 10) do?",
                        "options": ["A) Random float 1-10", "B) Random int 1-9", "C) Random int 1-10", "D) Random int 0-10"],
                        "answer": "C",
                        "explanation": "randint(a, b) returns random integer from a to b, inclusive"
                    }
                ]
            },
            {
                "title": "Exception Handling",
                "section": "PCEP Bonus Topic",
                "content": """
EXCEPTION HANDLING (basic level for PCEP):

try-except blocks handle errors gracefully:

try:
    # code that might raise exception
except ExceptionType:
    # handle specific exception
except:
    # handle any exception (not recommended)
else:
    # executes if no exception (optional)
finally:
    # always executes (optional)

COMMON EXCEPTIONS:
- ValueError: invalid value (e.g., int("abc"))
- TypeError: wrong type
- KeyError: dictionary key doesn't exist
- IndexError: list index out of range
- ZeroDivisionError: division by zero
- FileNotFoundError: file doesn't exist

RAISING EXCEPTIONS:
raise ExceptionType("error message")
                """,
                "example": """
# Basic try-except
try:
    x = int("abc")  # ValueError
except ValueError:
    print("Cannot convert to integer!")

# Multiple except blocks
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except ValueError:
    print("Value error occurred")
except IndexError:
    print("Index out of range!")

# Generic except (catches all)
try:
    result = 10 / 0
except:
    print("An error occurred")

# try-except-else-finally
try:
    value = int(input("Enter number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {value}")
finally:
    print("This always runs")

# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# Catching exception object
try:
    x = int("abc")
except ValueError as error:
    print(f"Caught: {error}")

# Safe input reading
while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Please enter a valid number")
                """,
                "exercise": {
                    "description": "Write a try-except block that attempts int conversion and catches ValueError",
                    "hint": "try: x = int('abc') except ValueError: print('Error')",
                    "check": lambda code: "try" in code.lower() and "except" in code.lower()
                },
                "quiz": [
                    {
                        "question": "Which exception is raised for int('hello')?",
                        "options": ["A) TypeError", "B) ValueError", "C) KeyError", "D) NameError"],
                        "answer": "B",
                        "explanation": "Invalid conversion to int raises ValueError"
                    },
                    {
                        "question": "When does the 'finally' block execute?",
                        "options": ["A) Only if no error", "B) Only if error", "C) Always", "D) Never"],
                        "answer": "C",
                        "explanation": "'finally' block always executes, regardless of exceptions"
                    },
                    {
                        "question": "What does 10 / 0 raise?",
                        "options": ["A) ValueError", "B) TypeError", "C) ZeroDivisionError", "D) ArithmeticError"],
                        "answer": "C",
                        "explanation": "Division by zero raises ZeroDivisionError"
                    }
                ]
            },
            {
                "title": "PCEP Bonus Questions - Study Guide Edition",
                "section": "PCEP Bonus",
                "content": """
PCEP EXAM PREPARATION: Comprehensive Bonus Questions

This bonus lesson contains 20 additional exam-style questions from the official
Certify4Sure PCEP-30-02 study guide. These questions represent real exam scenarios.

TOPICS COVERED:
- Python syntax and semantics
- Data types and operations
- Operators and precedence
- Control flow structures
- Data structures (lists, dictionaries, tuples, sets)
- Functions and scope
- Exception handling
- String operations and manipulation
- Input/output operations
- Modules and imports
- Number systems (binary, octal, hex)
- Object-oriented programming

EXAM STRATEGY FOR SUCCESS:
1. Read carefully - Pay attention to every word in the question
2. Identify topic - Determine what concept is being tested
3. Eliminate answers - Rule out obviously wrong options
4. Review explanations - Learn from each question answered
5. Track weak areas - Note topics where you're struggling
6. Practice consistently - Repetition builds mastery

This bonus section provides valuable practice for last-minute exam prep!
                """,
                "example": """
# Example 1: Operator precedence
result = 2 + 3 * 4  # Multiplication first: 2 + 12 = 14
print(result)

# Example 2: Type conversion
value = int("42")
text = str(3.14)
print(type(value), type(text))

# Example 3: List operations
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])   # [2, 3, 4]
print(numbers[-1])    # 5
print(len(numbers))   # 5

# Example 4: String methods
message = "Python Programming"
print(message.lower())      # python programming
print(message.split())      # ['Python', 'Programming']
print("o" in message)       # True
                """,
                "exercise": {
                    "description": "Create a function that takes two numbers and returns their sum, then call it with 5 and 7",
                    "hint": "def add(a, b): return a + b; print(add(5, 7))",
                    "check": lambda code: "def" in code and "return" in code
                },
                "quiz": [
                    {
                        "question": "Python is an example of which programming language category?",
                        "options": ["A) Interpreted", "B) Assembly", "C) Compiled", "D) Machine"],
                        "answer": "A",
                        "explanation": "Python is an interpreted language - code is executed by an interpreter at runtime."
                    },
                    {
                        "question": "A set of rules which defines the ways in which words can be coupled in sentences is called:",
                        "options": ["A) Lexis", "B) Syntax", "C) Semantics", "D) Dictionary"],
                        "answer": "B",
                        "explanation": "Syntax defines the rules for proper code structure and grammar."
                    },
                    {
                        "question": "What is the expected output of: len([1, 2, 3])?",
                        "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
                        "answer": "C",
                        "explanation": "len() returns the number of elements in a list. [1, 2, 3] has 3 elements."
                    },
                    {
                        "question": "What does the modulo operator (%) return?",
                        "options": ["A) Quotient", "B) Remainder", "C) Product", "D) Power"],
                        "answer": "B",
                        "explanation": "The % operator returns the remainder after division. 10 % 3 = 1"
                    },
                    {
                        "question": "Which of these is a mutable data type?",
                        "options": ["A) Tuple", "B) String", "C) List", "D) Integer"],
                        "answer": "C",
                        "explanation": "Lists are mutable - their contents can be changed. Tuples and strings are immutable."
                    },
                    {
                        "question": "What is the range of a while loop with condition 'while x < 5'?",
                        "options": ["A) x from 0 to 4", "B) x from 0 to 5", "C) Depends on x init", "D) Infinite"],
                        "answer": "C",
                        "explanation": "The range depends on the initial value of x and how it's modified in the loop."
                    },
                    {
                        "question": "How do you create an empty dictionary?",
                        "options": ["A) {}", "B) []", "C) ()", "D) None"],
                        "answer": "A",
                        "explanation": "Dictionaries use curly braces {}. An empty dictionary is {}."
                    },
                    {
                        "question": "What does the 'in' operator check?",
                        "options": ["A) Assignment", "B) Membership", "C) Comparison", "D) Type"],
                        "answer": "B",
                        "explanation": "'in' checks if a value exists in a sequence like lists, strings, or tuples."
                    },
                    {
                        "question": "Which exception is raised for division by zero?",
                        "options": ["A) ValueError", "B) TypeError", "C) ZeroDivisionError", "D) RuntimeError"],
                        "answer": "C",
                        "explanation": "Division by zero raises ZeroDivisionError: 10 / 0"
                    },
                    {
                        "question": "What is the output of: print(type(42))?",
                        "options": ["A) <class 'int'>", "B) int", "C) <int>", "D) 42"],
                        "answer": "A",
                        "explanation": "type() returns the class of an object as <class 'typename'>."
                    },
                    {
                        "question": "How do you access the last element of a list?",
                        "options": ["A) list[0]", "B) list[-1]", "C) list[end]", "D) list.last()"],
                        "answer": "B",
                        "explanation": "Negative indexing: list[-1] gives the last element, list[-2] the second-to-last, etc."
                    },
                    {
                        "question": "What does 'pass' do in Python?",
                        "options": ["A) Ends a loop", "B) Does nothing (null operation)", "C) Returns from function", "D) Continues loop"],
                        "answer": "B",
                        "explanation": "'pass' is a null operation - when executed, nothing happens. Used as placeholder."
                    },
                    {
                        "question": "Which keyword is used to create a function?",
                        "options": ["A) function", "B) func", "C) def", "D) define"],
                        "answer": "C",
                        "explanation": "The 'def' keyword defines a function in Python."
                    },
                    {
                        "question": "What is a lambda function?",
                        "options": ["A) Named function", "B) Anonymous function", "C) Built-in function", "D) Class method"],
                        "answer": "B",
                        "explanation": "Lambda creates small anonymous functions: lambda x: x * 2"
                    },
                    {
                        "question": "How do you convert string '42' to integer?",
                        "options": ["A) str(42)", "B) int('42')", "C) convert('42')", "D) '42'.int()"],
                        "answer": "B",
                        "explanation": "int() converts a string to an integer. int('42') returns 42"
                    },
                    {
                        "question": "What does the split() method do?",
                        "options": ["A) Joins strings", "B) Replaces characters", "C) Splits into list", "D) Checks length"],
                        "answer": "C",
                        "explanation": "'hello world'.split() returns ['hello', 'world'] - splits by whitespace."
                    },
                    {
                        "question": "Which loop is best for iterating over a list?",
                        "options": ["A) while loop", "B) for loop", "C) do-while loop", "D) goto loop"],
                        "answer": "B",
                        "explanation": "for loops are preferred for iterating over sequences like lists and strings."
                    },
                    {
                        "question": "What does 'elif' stand for?",
                        "options": ["A) else if", "B) electric if", "C) elif is standalone", "D) else loop"],
                        "answer": "A",
                        "explanation": "'elif' is short for 'else if' and provides additional conditions to check."
                    },
                    {
                        "question": "How do you add an element to a list?",
                        "options": ["A) list.add(item)", "B) list.append(item)", "C) list.push(item)", "D) list += item"],
                        "answer": "B",
                        "explanation": ".append() adds a single element to the end of a list."
                    },
                    {
                        "question": "What is the correct way to write a docstring?",
                        "options": ["A) # comment", "B) // comment", "C) \"\"\"docstring\"\"\"", "D) -- comment"],
                        "answer": "C",
                        "explanation": "Docstrings use triple quotes: \"\"\"This is a docstring\"\"\""
                    }
                ]
            }
        ]
        
        # Add quiz bank for practice exams
        self.practice_questions = self._generate_practice_bank()
    
    def _generate_practice_bank(self):
        """Generate pool of all quiz questions plus PDF study guide questions for practice exams"""
        questions = []
        
        # Add all lesson quiz questions
        for lesson in self.lessons:
            if "quiz" in lesson:
                for q in lesson["quiz"]:
                    questions.append({
                        **q,
                        "topic": lesson["title"]
                    })
        
        # Add all 183 questions from PCEP study guide PDF
        pdf_study_questions = self._load_pdf_study_questions()
        questions.extend(pdf_study_questions)
        
        return questions
    
    def _load_pdf_study_questions(self):
        """Load 183 PCEP exam questions from study guide"""
        pdf_json_path = os.path.join(os.path.dirname(__file__), "PCEP_Questions.json")
        
        if not os.path.exists(pdf_json_path):
            return []
        
        try:
            with open(pdf_json_path, 'r') as f:
                pdf_questions = json.load(f)
            
            formatted_questions = []
            for q in pdf_questions:
                options = []
                if isinstance(q.get('options'), dict):
                    for key in sorted(q['options'].keys()):
                        options.append(q['options'][key])
                
                # Get correct answer index
                answer_key = q.get('correct_answer', 'A')
                answer_key = answer_key[0] if answer_key else 'A'
                correct_idx = ord(answer_key) - ord('A') if answer_key in 'ABCD' else 0
                
                # Ensure we have 4 options
                while len(options) < 4:
                    options.append("")
                
                formatted_questions.append({
                    "question": q.get('question_text', '')[:150],
                    "options": options[:4],
                    "correct": correct_idx,
                    "answer": answer_key,
                    "explanation": q.get('explanation', 'See study guide for details.')[:300],
                    "topic": "PDF Study Guide"
                })
            
            return formatted_questions
        except Exception:
            return []
    
    def load_progress(self):
        """Load user's progress from file"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    data = json.load(f)
                    self.current_lesson = data.get('current_lesson', 0)
                    self.completed_lessons = set(data.get('completed_lessons', []))
                    self.quiz_scores = data.get('quiz_scores', {})
            except Exception:
                pass
    
    def save_progress(self):
        """Save user's progress to file"""
        try:
            with open(self.progress_file, 'w') as f:
                json.dump({
                    'current_lesson': self.current_lesson,
                    'completed_lessons': list(self.completed_lessons),
                    'quiz_scores': self.quiz_scores
                }, f, indent=2)
        except Exception:
            pass
    
    def clear_screen(self):
        """Clear the terminal screen"""
        import subprocess
        try:
            if os.name == 'nt':
                subprocess.run(['cls'], shell=False, check=False)
            else:
                subprocess.run(['clear'], shell=False, check=False)
        except Exception:
            pass
    
    def display_menu(self):
        """Display main menu"""
        self.clear_screen()
        print("=" * 70)
        print("  🎓 PCEP PYTHON CERTIFICATION EXAM TUTOR")
        print("  Python Certified Entry-Level Programmer Preparation")
        print("=" * 70)
        
        # Calculate overall progress
        total_lessons = len(self.lessons)
        completed = len(self.completed_lessons)
        progress_pct = (completed / total_lessons * 100) if total_lessons > 0 else 0
        
        # Calculate quiz performance
        total_quiz_score = sum(self.quiz_scores.values())
        total_quizzes = len(self.quiz_scores)
        avg_score = (total_quiz_score / total_quizzes) if total_quizzes > 0 else 0
        
        print(f"\n📊 Progress: {completed}/{total_lessons} lessons ({progress_pct:.0f}%)", end="")
        if total_quizzes > 0:
            print(f" | Quiz Average: {avg_score:.0f}%")
        else:
            print()
        
        # Group lessons by section
        current_section = ""
        for i, lesson in enumerate(self.lessons):
            section = lesson.get("section", "")
            if section != current_section:
                print(f"\n{section}:")
                current_section = section
            
            status = "✓" if i in self.completed_lessons else " "
            current = "→ " if i == self.current_lesson else "  "
            
            # Show quiz score if available
            quiz_info = ""
            if str(i) in self.quiz_scores:
                quiz_info = f" [Quiz: {self.quiz_scores[str(i)]}%]"
            
            print(f"{current}[{status}] {i+1}. {lesson['title']}{quiz_info}")
        
        print("\n" + "=" * 70)
        print("\n📚 Commands:")
        print("  [number] - Go to lesson")
        print("  n - Next lesson | p - Previous lesson")
        print("  e - Take practice exam (20 random questions)")
        print("  s - Show study tips | r - Reset progress | q - Quit")
        print("=" * 70)
    
    def display_lesson(self, lesson_num):
        """Display a lesson with example and exercise"""
        if lesson_num < 0 or lesson_num >= len(self.lessons):
            return
        
        lesson = self.lessons[lesson_num]
        self.clear_screen()
        
        print("=" * 70)
        print(f"  LESSON {lesson_num + 1}: {lesson['title']}")
        print(f"  {lesson.get('section', '')}")
        print("=" * 70)
        
        print("\n📚 LESSON CONTENT:")
        print(lesson['content'])
        
        print("\n💡 EXAMPLE CODE:")
        print("-" * 70)
        print(lesson['example'])
        print("-" * 70)
        
        print("\n✏️  EXERCISE:")
        print(lesson['exercise']['description'])
        print(f"💭 Hint: {lesson['exercise']['hint']}")
        
        # Show quiz info if available
        if "quiz" in lesson:
            print(f"\n📝 Quiz available ({len(lesson['quiz'])} questions)")
        
        print("\n" + "=" * 70)
        print("Options:")
        print("  t - Try the example code")
        print("  e - Do the exercise")
        if "quiz" in lesson:
            print("  q - Take the quiz for this lesson")
        print("  m - Back to menu")
        print("=" * 70)
    
    def run_example(self, lesson_num):
        """Run the example code for a lesson"""
        lesson = self.lessons[lesson_num]
        print("\n🔧 Running example code...\n")
        print("-" * 70)
        
        try:
            # Use restricted namespace for safer code execution
            restricted_globals = {
                '__builtins__': {
                    'print': print, 'len': len, 'range': range, 
                    'enumerate': enumerate, 'zip': zip, 'list': list, 
                    'dict': dict, 'set': set, 'tuple': tuple, 'str': str, 
                    'int': int, 'float': float, 'bool': bool, 'type': type, 
                    'max': max, 'min': min, 'sum': sum, 'sorted': sorted, 
                    'reversed': reversed, 'filter': filter, 'map': map
                }
            }
            exec(lesson['example'], restricted_globals)
        except Exception as e:
            print(f"Error: {e}")
        
        print("-" * 70)
        input(self.PRESS_ENTER_NEWLINE)
    
    def take_quiz(self, lesson_num):
        """Take quiz for specific lesson"""
        lesson = self.lessons[lesson_num]
        if "quiz" not in lesson:
            print("\nNo quiz available for this lesson.")
            input(self.PRESS_ENTER)
            return
        
        quiz = lesson["quiz"]
        print("\n" + "=" * 70)
        print(f"  📝 QUIZ: {lesson['title']}")
        print("=" * 70)
        print(f"\nThis quiz has {len(quiz)} questions. Answer carefully!")
        print("Enter A, B, C, or D for each question.\n")
        input("Press Enter to start...")
        
        correct = 0
        for i, q in enumerate(quiz, 1):
            self.clear_screen()
            print(f"\n📝 Question {i}/{len(quiz)}:\n")
            print(q["question"])
            print()
            for opt in q["options"]:
                print(f"  {opt}")
            print()
            
            while True:
                answer = input("Your answer (A/B/C/D): ").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                print("Please enter A, B, C, or D")
            
            if answer == q["answer"]:
                print("\n✅ Correct!")
                correct += 1
            else:
                print(f"\n❌ Incorrect. The correct answer is {q['answer']}")
            
            print(f"\n💡 Explanation: {q['explanation']}")
            input("\nPress Enter for next question...")
        
        # Calculate score
        score = int((correct / len(quiz)) * 100)
        self.quiz_scores[str(lesson_num)] = score
        self.save_progress()
        
        # Show results
        self.clear_screen()
        print("\n" + "=" * 70)
        print("  📊 QUIZ RESULTS")
        print("=" * 70)
        print(f"\nYou got {correct} out of {len(quiz)} questions correct!")
        print(f"Score: {score}%\n")
        
        if score >= 80:
            print("🎉 Excellent work! You've mastered this topic!")
            self.completed_lessons.add(lesson_num)
            self.save_progress()
        elif score >= 60:
            print("👍 Good job! Review the lesson to improve further.")
        else:
            print("📚 Keep studying! Review the lesson and try again.")
        
        input(self.PRESS_ENTER_NEWLINE)
    
    def do_exercise(self, lesson_num):
        """Interactive exercise for a lesson"""
        lesson = self.lessons[lesson_num]
        exercise = lesson['exercise']
        
        print("\n" + "=" * 70)
        print("EXERCISE MODE")
        print("=" * 70)
        print(f"\n{exercise['description']}")
        print(f"💭 Hint: {exercise['hint']}")
        print("\nType your Python code below. Type 'done' on a new line when finished.")
        print("Type 'cancel' to go back.")
        print("-" * 70)
        
        code_lines = []
        while True:
            try:
                line = input(">>> " if not code_lines else "... ")
                if line.strip().lower() == 'done':
                    break
                elif line.strip().lower() == 'cancel':
                    return
                code_lines.append(line)
            except (EOFError, KeyboardInterrupt):
                return
        
        user_code = "\n".join(code_lines)
        
        # Check if exercise is correct
        if exercise['check'](user_code):
            print("\n✅ Great job! Your solution looks good!")
            print("\nLet's run it:")
            print("-" * 70)
            try:
                exec(user_code)
            except Exception as e:
                print(f"Runtime error: {e}")
            print("-" * 70)
            
            print("\n🎉 Exercise completed!")
        else:
            print("\n⚠️  Your code doesn't quite match the exercise requirements.")
            print("💭 Check the hint and try again!")
        
        input(self.PRESS_ENTER_NEWLINE)
    
    def _ask_exam_question(self, i, q):
        """Ask a single exam question and return answer"""
        self.clear_screen()
        print(f"\n📝 Question {i}/20:\n")
        print(q["question"])
        print()
        for opt in q["options"]:
            print(f"  {opt}")
        print()
        
        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            print("Please enter A, B, C, or D")
    
    def _show_exam_results(self, correct, results):
        """Display exam results and review incorrect answers"""
        score = int((correct / 20) * 100)
        
        self.clear_screen()
        print("\n" + "=" * 70)
        print("  📊 PRACTICE EXAM RESULTS")
        print("=" * 70)
        print(f"\nYou got {correct} out of 20 questions correct!")
        print(f"Score: {score}%\n")
        
        if score >= 70:
            print("🎉 PASS! You're ready for the PCEP exam!")
        else:
            print("📚 Keep studying! Review weak areas and try again.")
        
        print(f"\nPassing score: 70% (You scored: {score}%)")
        
        # Show incorrect answers
        print("\n" + "=" * 70)
        print("Review Incorrect Answers:")
        print("=" * 70)
        
        for i, r in enumerate(results, 1):
            if not r["is_correct"]:
                print(f"\n❌ Q{i}: {r['question']}")
                print(f"   Your answer: {r['your_answer']}")
                print(f"   Correct: {r['correct_answer']}")
                print(f"   Topic: {r['topic']}")
                print(f"   Explanation: {r['explanation']}")
        
        input(self.PRESS_ENTER_NEWLINE)
    
    def take_practice_exam(self):
        """Take a practice exam with random questions"""
        if len(self.practice_questions) < 20:
            print("\nNot enough questions available for practice exam.")
            input(self.PRESS_ENTER)
            return
        
        # Select 20 random questions
        questions = random.sample(self.practice_questions, 20)
        
        print("\n" + "=" * 70)
        print("  🎯 PCEP PRACTICE EXAM")
        print("=" * 70)
        print("\nThis practice exam has 20 questions covering all PCEP topics.")
        print("Passing score: 70%")
        print("\nAnswer carefully - this simulates the real exam!")
        input(self.PRESS_ENTER_NEWLINE)
        
        correct = 0
        results = []
        
        for i, q in enumerate(questions, 1):
            answer = self._ask_exam_question(i, q)
            is_correct = (answer == q["answer"])
            
            if is_correct:
                correct += 1
            
            results.append({
                "question": q["question"],
                "your_answer": answer,
                "correct_answer": q["answer"],
                "is_correct": is_correct,
                "explanation": q["explanation"],
                "topic": q["topic"]
            })
        
        self._show_exam_results(correct, results)
    
    def show_study_tips(self):
        """Display PCEP exam study tips"""
        self.clear_screen()
        print("=" * 70)
        print("  📖 PCEP EXAM STUDY TIPS")
        print("=" * 70)
        print("""
ABOUT THE PCEP EXAM:
- 30 multiple-choice questions
- 40 minutes
- Passing score: 70%
- Online proctored exam

EXAM SECTIONS:
1. Basic Concepts (18%)
   - Compilation vs interpretation
   - Python fundamentals
   
2. Data Types, Variables, I/O, Operators (29%)
   - Literals and variables
   - Operators and expressions
   - Strings and I/O
   
3. Boolean, Conditionals, Loops, Lists, Logic (25%)
   - Boolean values
   - Conditional execution
   - Loops (for, while)
   - Lists and operations
   - Logical and bitwise operators
   
4. Functions, Tuples, Dictionaries, Modules (28%)
   - Function definition and calling
   - Tuples
   - Dictionaries
   - Importing modules

STUDY STRATEGIES:
✓ Complete all lessons and quizzes (aim for 80%+ on quizzes)
✓ Take multiple practice exams
✓ Focus on weak areas
✓ Practice coding exercises regularly
✓ Understand operator precedence
✓ Know the difference between mutable and immutable types
✓ Be familiar with common built-in functions
✓ Understand indexing and slicing thoroughly

EXAM TIPS:
✓ Read questions carefully
✓ Eliminate obviously wrong answers first
✓ Watch out for tricky wording
✓ Pay attention to syntax details (case sensitivity, colons, etc.)
✓ Manage your time (45 seconds per question average)
✓ Review flagged questions if time permits

KEY THINGS TO MEMORIZE:
- Operator precedence: ** > unary > * / // % > + -
- Logical precedence: not > and > or
- String/list indexing and slicing
- Common built-in functions: len(), type(), range(), etc.
- Module import syntax variations
- Mutable vs immutable types
- Boolean truthy/falsy values
        """)
        input(self.PRESS_ENTER_NEWLINE)
    
    def _handle_navigation_choice(self, choice):
        """Handle navigation commands (n, p)"""
        if choice == 'n' and self.current_lesson < len(self.lessons) - 1:
            self.current_lesson += 1
            return True
        if choice == 'p' and self.current_lesson > 0:
            self.current_lesson -= 1
            return True
        return False
    
    def _handle_reset_progress(self):
        """Handle progress reset command"""
        confirm = input("Are you sure you want to reset progress? (yes/no): ")
        if confirm.lower() == 'yes':
            self.completed_lessons.clear()
            self.quiz_scores.clear()
            self.current_lesson = 0
            self.save_progress()
            print("Progress reset!")
            input(self.PRESS_ENTER)
    
    def _handle_lesson_choice(self, choice):
        """Handle numeric lesson selection"""
        lesson_num = int(choice) - 1
        if 0 <= lesson_num < len(self.lessons):
            self.current_lesson = lesson_num
            self.lesson_mode(lesson_num)
            return True
        return False
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            
            choice = input("\nYour choice: ").strip().lower()
            
            if choice == 'q':
                print("\n👋 Good luck on your PCEP exam! Keep coding!")
                break
            elif self._handle_navigation_choice(choice):
                continue
            elif choice == 'e':
                self.take_practice_exam()
            elif choice == 's':
                self.show_study_tips()
            elif choice == 'r':
                self._handle_reset_progress()
            elif choice.isdigit():
                self._handle_lesson_choice(choice)
            else:
                print("Invalid choice!")
                input(self.PRESS_ENTER)
    
    def lesson_mode(self, lesson_num):
        """Interactive mode for a specific lesson"""
        while True:
            self.display_lesson(lesson_num)
            choice = input("\nYour choice: ").strip().lower()
            
            if choice == 'm':
                break
            elif choice == 't':
                self.run_example(lesson_num)
            elif choice == 'e':
                self.do_exercise(lesson_num)
            elif choice == 'q' and "quiz" in self.lessons[lesson_num]:
                self.take_quiz(lesson_num)
            else:
                print("Invalid choice!")
                input(self.PRESS_ENTER)


def main():
    """Entry point for the application"""
    tutor = PythonTutor()
    try:
        tutor.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()


# Additional Practice Questions and Code Examples
ADDITIONAL_QUESTIONS = [
    {
        "question": "What will this code output?\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "Error", "[4]"],
        "correct": 1,
        "explanation": "Lists are mutable and passed by reference. y points to the same list as x, so changes to y affect x."
    },
    {
        "question": "Which of the following is an immutable type in Python?",
        "options": ["list", "dict", "tuple", "set"],
        "correct": 2,
        "explanation": "Tuples are immutable. Lists, dicts, and sets can all be modified after creation."
    },
    {
        "question": "What does len('hello') return?",
        "options": ["4", "5", "6", "Error"],
        "correct": 1,
        "explanation": "The len() function returns the number of characters in a string. 'hello' has 5 characters."
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": ["3.33", "3", "4", "3.333333"],
        "correct": 1,
        "explanation": "The // operator performs floor division, returning the integer quotient without remainder."
    },
    {
        "question": "What will this code output?\nfor i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0\\n1\\n2", "Error"],
        "correct": 2,
        "explanation": "range(3) generates 0, 1, 2. Each print() creates a new line by default."
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "define", "func"],
        "correct": 1,
        "explanation": "The 'def' keyword defines a function in Python."
    },
    {
        "question": "What is the result of: 'py' * 3?",
        "options": ["pypy", "pypy", "pypy", "Error"],
        "correct": 1,
        "explanation": "Multiplying a string by an integer repeats (concatenates) the string that many times."
    },
    {
        "question": "What will this code output?\nx = 5\nif x > 3:\n    print('yes')\nelse:\n    print('no')",
        "options": ["yes", "no", "Error", "yesno"],
        "correct": 0,
        "explanation": "5 > 3 is True, so the if block executes and prints 'yes'."
    },
    {
        "question": "Which of these is a valid variable name in Python?",
        "options": ["123abc", "_abc123", "abc-123", "abc 123"],
        "correct": 1,
        "explanation": "Variable names can start with a letter or underscore, followed by letters, numbers, or underscores."
    },
    {
        "question": "What is type(3.14)?",
        "options": ["int", "float", "number", "decimal"],
        "correct": 1,
        "explanation": "3.14 is a floating-point number, so type() returns <class 'float'>."
    },
    {
        "question": "What will this output?\nprint(True + True)?",
        "options": ["2", "True", "Error", "1"],
        "correct": 0,
        "explanation": "In Python, True is equivalent to 1 and False to 0 in arithmetic operations. 1 + 1 = 2."
    },
    {
        "question": "What does 'in' operator do?",
        "options": ["Creates a variable", "Checks membership", "Assigns value", "Compares equality"],
        "correct": 1,
        "explanation": "The 'in' operator checks if a value exists in a sequence (string, list, tuple, etc.)."
    },
    {
        "question": "What is the output of: list('abc')?",
        "options": ["'abc'", "['a', 'b', 'c']", "Error", "['abc']"],
        "correct": 1,
        "explanation": "list() converts an iterable into a list. For a string, it separates into individual characters."
    },
    {
        "question": "Which method adds an element to a list?",
        "options": ["add()", "append()", "insert()", "push()"],
        "correct": 1,
        "explanation": "The append() method adds a single element to the end of a list."
    },
    {
        "question": "What does import sys do?",
        "options": ["Imports a module", "Creates a system", "Exits the program", "Error"],
        "correct": 0,
        "explanation": "import loads a module. 'sys' is a module providing access to system-specific parameters."
    }
]

CODE_PRACTICE = {
    "practice_1": {
        "title": "Basic String Operations",
        "description": "Practice working with strings",
        "code": """
# String concatenation
greeting = "Hello" + " " + "World"
print(greeting)

# String methods
text = "PYTHON"
print(text.lower())
print(text.replace("P", "J"))

# String indexing
word = "PCEP"
print(word[0])  # First character
print(word[-1])  # Last character
print(word[1:3])  # Substring
"""
    },
    "practice_2": {
        "title": "Working with Lists",
        "description": "Practice list operations",
        "code": """
# List operations
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.extend([7, 8])
print(numbers)

# List indexing and slicing
print(numbers[0])
print(numbers[-2])
print(numbers[1:4])

# List methods
numbers.remove(3)
numbers.reverse()
print(numbers)
"""
    },
    "practice_3": {
        "title": "Loops and Conditionals",
        "description": "Practice control flow",
        "code": """
# For loop
for i in range(1, 6):
    print(f"Number: {i}")

# While loop
x = 5
while x > 0:
    print(x)
    x -= 1

# Nested conditionals
age = 25
if age >= 18:
    print("Adult")
    if age >= 65:
        print("Senior")
else:
    print("Minor")
"""
    },
    "practice_4": {
        "title": "Functions",
        "description": "Practice defining and calling functions",
        "code": """
# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with multiple parameters
def add(a, b):
    return a + b

print(add(5, 3))

# Function with default parameter
def power(base, exp=2):
    return base ** exp

print(power(3))
print(power(3, 3))
"""
    },
    "practice_5": {
        "title": "Dictionaries",
        "description": "Practice working with dictionaries",
        "code": """
# Create a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person["name"])

# Add/modify items
person["job"] = "Engineer"
person["age"] = 31

# Dictionary methods
print(person.keys())
print(person.values())
print(person.items())

# Check if key exists
if "name" in person:
    print("Name exists")
"""
    }
}

# Extended Practice Questions Set 2
EXTENDED_QUESTIONS = [
    {
        "question": "What is the output of: print(5 == 5.0)?",
        "options": ["True", "False", "Error", "None"],
        "correct": 0,
        "explanation": "In Python, 5 and 5.0 are equal in value. The == operator checks value equality."
    },
    {
        "question": "Which of the following creates an empty list?",
        "options": ["[]", "list()", "[None]", "Both A and B"],
        "correct": 3,
        "explanation": "Both [] and list() create empty lists. They are equivalent."
    },
    {
        "question": "What does enumerate() do?",
        "options": ["Counts items", "Adds index to items", "Removes duplicates", "Sorts items"],
        "correct": 1,
        "explanation": "enumerate() returns pairs of (index, item) for each element in an iterable."
    },
    {
        "question": "What is the output of: 'test'.upper()?",
        "options": ["'test'", "'TEST'", "Error", "'Test'"],
        "correct": 1,
        "explanation": "The upper() method converts all characters in a string to uppercase."
    },
    {
        "question": "What does break do in a loop?",
        "options": ["Pauses the loop", "Exits the loop", "Restarts the loop", "Skips iteration"],
        "correct": 1,
        "explanation": "break exits the loop immediately, regardless of the loop condition."
    },
    {
        "question": "What is the output of: print([1,2,3] + [4,5])?",
        "options": ["[1,2,3,4,5]", "Error", "[1,2,3] [4,5]", "[1,2,3+4,5]"],
        "correct": 0,
        "explanation": "The + operator concatenates lists, combining them into a single list."
    },
    {
        "question": "What does continue do in a loop?",
        "options": ["Exits the loop", "Skips to next iteration", "Pauses execution", "Error"],
        "correct": 1,
        "explanation": "continue skips the current iteration and moves to the next one."
    },
    {
        "question": "Which is a valid Python comment?",
        "options": ["// comment", "# comment", "/* comment */", "-- comment"],
        "correct": 1,
        "explanation": "Python uses # for single-line comments."
    },
    {
        "question": "What is the output of: print(2 ** 3 ** 2)?",
        "options": ["512", "64", "128", "256"],
        "correct": 0,
        "explanation": "Exponentiation is right-associative: 2 ** (3 ** 2) = 2 ** 9 = 512."
    },
    {
        "question": "What does sorted() return?",
        "options": ["None", "A sorted list", "Modifies original", "Error"],
        "correct": 1,
        "explanation": "sorted() returns a new sorted list without modifying the original."
    },
    {
        "question": "What is the output of: print({1, 2, 2, 3})?",
        "options": ["{1, 2, 2, 3}", "{1, 2, 3}", "Error", "[1, 2, 3]"],
        "correct": 1,
        "explanation": "Sets automatically remove duplicates. {1, 2, 2, 3} becomes {1, 2, 3}."
    },
    {
        "question": "What does max([3,1,4,1,5]) return?",
        "options": ["1", "3", "5", "Error"],
        "correct": 2,
        "explanation": "max() returns the largest item in an iterable."
    },
    {
        "question": "What does min([3,1,4,1,5]) return?",
        "options": ["1", "3", "4", "5"],
        "correct": 0,
        "explanation": "min() returns the smallest item in an iterable."
    },
    {
        "question": "What does sum([1,2,3,4]) return?",
        "options": ["10", "9", "11", "Error"],
        "correct": 0,
        "explanation": "sum() returns the total of all items. 1+2+3+4 = 10."
    },
    {
        "question": "What is the output of: print('a' in 'apple')?",
        "options": ["True", "False", "Error", "None"],
        "correct": 0,
        "explanation": "The 'in' operator checks if 'a' is in the string 'apple'. It is."
    },
    {
        "question": "What does split() do?",
        "options": ["Joins strings", "Splits string into list", "Removes characters", "Error"],
        "correct": 1,
        "explanation": "split() breaks a string into a list based on a delimiter (default is space)."
    },
    {
        "question": "What does join() do?",
        "options": ["Splits strings", "Combines list into string", "Removes spaces", "Error"],
        "correct": 1,
        "explanation": "join() combines a list of strings into a single string with a separator."
    },
    {
        "question": "What is the output of: print(abs(-5))?",
        "options": ["-5", "5", "Error", "0"],
        "correct": 1,
        "explanation": "abs() returns the absolute value (distance from zero)."
    },
    {
        "question": "What does round(3.7) return?",
        "options": ["3", "3.7", "4", "3.0"],
        "correct": 2,
        "explanation": "round() rounds to the nearest integer. 3.7 rounds up to 4."
    },
    {
        "question": "What is the output of: print(isinstance(5, int))?",
        "options": ["True", "False", "Error", "5"],
        "correct": 0,
        "explanation": "isinstance() checks if an object is an instance of a class. 5 is an int."
    }
]

# Extended Code Practice Examples
EXTENDED_PRACTICE = {
    "practice_6": {
        "title": "Exception Handling",
        "description": "Practice try-except blocks",
        "code": """
# Basic try-except
try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Try with multiple exceptions
try:
    number = int("abc")
except ValueError:
    print("Invalid number format")
except Exception as e:
    print(f"Error: {e}")

# Try-except-else
try:
    x = 5
except ValueError:
    print("Error occurred")
else:
    print("No error, x =", x)
"""
    },
    "practice_7": {
        "title": "List Comprehensions",
        "description": "Practice list comprehensions",
        "code": """
# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Nested list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)

# List comprehension with string
chars = [c.upper() for c in "hello"]
print(chars)  # ['H', 'E', 'L', 'L', 'O']
"""
    },
    "practice_8": {
        "title": "Lambda Functions",
        "description": "Practice lambda expressions",
        "code": """
# Simple lambda
square = lambda x: x ** 2
print(square(5))

# Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 4))

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Lambda with sorted()
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
"""
    },
    "practice_9": {
        "title": "Working with Tuples",
        "description": "Practice tuple operations",
        "code": """
# Creating tuples
single = (1,)  # Note the comma for single element
pair = (1, 2)
triple = (1, 2, 3)

# Tuple unpacking
x, y, z = (1, 2, 3)
print(x, y, z)

# Tuples are immutable
t = (1, 2, 3)
# t[0] = 5  # This would cause an error

# Tuple operations
print(len(t))
print(t[0])
print(t[-1])
print(1 in t)

# Converting between lists and tuples
lst = [1, 2, 3]
tup = tuple(lst)
lst2 = list(tup)
"""
    },
    "practice_10": {
        "title": "Set Operations",
        "description": "Practice working with sets",
        "code": """
# Creating sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Set operations
union = s1 | s2
intersection = s1 & s2
difference = s1 - s2
symmetric_diff = s1 ^ s2

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")

# Set methods
s1.add(5)
s1.remove(1)
s1.discard(10)  # Won't error if not present

# Checking membership
if 2 in s1:
    print("2 is in the set")
"""
    },
    "practice_11": {
        "title": "String Formatting",
        "description": "Practice different string formatting methods",
        "code": """
# Old-style formatting
name = "Alice"
age = 30
formatted1 = "%s is %d years old" % (name, age)
print(formatted1)

# str.format() method
formatted2 = "{} is {} years old".format(name, age)
print(formatted2)

# f-strings (Python 3.6+)
formatted3 = f"{name} is {age} years old"
print(formatted3)

# f-strings with expressions
x = 10
y = 20
print(f"Sum: {x + y}")
print(f"Max: {max(x, y)}")

# Formatting numbers
pi = 3.14159
print(f"Pi: {pi:.2f}")  # 2 decimal places
"""
    },
    "practice_12": {
        "title": "Importing and Modules",
        "description": "Practice importing and using modules",
        "code": """
# Import entire module
import math
print(math.pi)
print(math.sqrt(16))

# Import specific functions
from math import sqrt, pow
print(sqrt(25))
print(pow(2, 3))

# Import with alias
import math as m
print(m.ceil(3.2))

# Import all (use with caution)
# from math import *

# Using collections module
from collections import Counter
words = "hello world"
counter = Counter(words)
print(counter)  # Shows character frequencies
"""
    },
    "practice_13": {
        "title": "Working with Files",
        "description": "Practice file operations",
        "code": """
# Writing to a file
with open("output.txt", "w") as f:
    f.write("Hello, World!\\n")
    f.write("Second line\\n")

# Reading from a file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())

# Appending to a file
with open("output.txt", "a") as f:
    f.write("Appended line\\n")
"""
    },
    "practice_14": {
        "title": "Class Definition Basics",
        "description": "Practice defining and using classes",
        "code": """
# Define a class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def birthday(self):
        self.age += 1

# Create instances
dog1 = Dog("Rex", 3)
dog2 = Dog("Buddy", 5)

# Use methods and attributes
print(dog1.name)
print(dog1.bark())
dog1.birthday()
print(dog1.age)
"""
    },
    "practice_15": {
        "title": "Advanced Loops",
        "description": "Practice while loops and loop control",
        "code": """
# While loop with counter
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with break
num = 0
while True:
    if num == 5:
        break
    print(num)
    num += 1

# While loop with continue
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)  # Only prints odd numbers

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
"""
    }
}
