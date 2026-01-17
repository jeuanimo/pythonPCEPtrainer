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
                    "hint": "def add(a, b): return a + b\nprint(add(5, 7))",
                    "check": lambda code: "def" in code and "return" in code
                },
                "quiz": [
                    {
                        "question": "DRAG DROP Insert the code boxes in the correct positions in order to build a line of code which asks the user for an integer value and assig",
                        "options": ["A) Option A", "B) Option B", "C) Option C", "D) Option D"],
                        "answer": "A",
                        "explanation": "One possible way to insert the code boxes in the correct positions in order to build a line of code which asks the user for an integer value and assigns it to the depth variable is: depth = int(input(\"Enter the immersion depth: \")) This line of cod"
                    },
                    {
                        "question": "A set of rules which defines the ways in which words can be coupled in sentences is called:",
                        "options": ["A) lexis", "B) syntax", "C) semantics", "D) dictionary"],
                        "answer": "B",
                        "explanation": "Syntax is the branch of linguistics that studies the structure and rules of sentences in natural languages. Lexis is the vocabulary of a language. Semantics is the study of meaning in language. A dictionary is a collection of words and their definiti"
                    },
                    {
                        "question": "Which of the following expressions evaluate to a non-zero result? (Select two answers.)",
                        "options": ["A) 2 ** 3 / A - 2", "B) 4 / 2 * * 3 - 2", "C) 1 * * 3 / 4 - 1", "D) 1 * 4 // 2 ** 3"],
                        "answer": "A",
                        "explanation": "In Python, the ** operator is used for exponentiation, the / operator is used for floating-point division, and the // operator is used for integer division. The order of operations is parentheses, exponentiation, multiplication/ division, and additio"
                    },
                    {
                        "question": "Python Is an example of which programming language category?",
                        "options": ["A) interpreted", "B) assembly", "C) compiled", "D) machine"],
                        "answer": "A",
                        "explanation": "Python is an interpreted programming language, which means that the source code is translated into executable code by an interpreter at runtime, rather than by a compiler beforehand. Interpreted languages are more flexible and portable than compiled "
                    },
                    {
                        "question": "How many hashes (+) does the code output to the screen?  floor = 10 while floor != 0: floor //= 4 print (\"#\", end=””) else: print (\"#\")",
                        "options": ["A) one", "B) zero (the code outputs nothing)", "C) five", "D) three"],
                        "answer": "C",
                        "explanation": "The code snippet that you have sent is a loop that checks if a variable oefloor is less than or equal to 0 and prints a string accordingly. The code is as follows: floor = 5 while floor > 0: print(oe+ ) floor = floor - 1 The code starts with assignin"
                    },
                    {
                        "question": "What happens when the user runs the following code?",
                        "options": ["A) The code outputs 3.", "B) The code outputs 2.", "C) The code enters an infinite loop.", "D) The code outputs 1."],
                        "answer": "B",
                        "explanation": "The code snippet that you have sent is calculating the value of a variable oetotal based on the values in the range of 0 to 3. The code is as follows: total = 0 for i in range(0, 3): if i % 2 == 0: total = total + 1 else: total = total + 2 print(tota"
                    },
                    {
                        "question": "What is the expected output of the following code?",
                        "options": ["A) The code produces no output.", "B) * * *", "C) * *", "D) *"],
                        "answer": "C",
                        "explanation": "The code snippet that you have sent is a conditional statement that checks if a variable oecounter is less than 0, greater than or equal to 42, or neither. The code is as follows: if counter < 0: print(oeoe) elif counter >= 42: print( oe) else: print"
                    },
                    {
                        "question": "What happens when the user runs the following code?",
                        "options": ["A) The program outputs three asterisks ( *** )to the screen.", "B) The program outputs one asterisk ( * ) to the screen.", "C) The program outputs five asterisks ( ***** ) to the screen.", "D) The program enters an infinite loop."],
                        "answer": "D",
                        "explanation": "The code snippet that you have sent is a while loop with an if statement and a print statement inside it. The code is as follows: while True: if counter < 0: print(*) else: print( ** ) The code starts with entering a while loop that repeats indefinit"
                    },
                    {
                        "question": "What is the expected output of the following code?  equals = 0 for i in range (2): for j in range (2): if i == j: equals += 1 else: equals ",
                        "options": ["A) The code outputs nothing.", "B) 3", "C) 1", "D) 4"],
                        "answer": "C",
                        "explanation": "The code snippet that you have sent is checking if two numbers are equal and printing the result. The code is as follows: num1 = 1 num2 = 2 if num1 == num2: print(4) else: print(1) The code starts with assigning the values 1 and 2 to the variables oe"
                    },
                    {
                        "question": "What is the expected output of the following code?  collection = [ ] collection.append(1) collection.insert(0, 2) duplicate = collection dup",
                        "options": ["B) 4", "C) 6", "D) The code raises an exception and outputs nothing."],
                        "answer": "D",
                        "explanation": "The code snippet that you have sent is trying to print the combined length of two lists, oecollection and oeduplicate . The code is as follows: collection = [] collection.append(1) collection.insert(0, 2) duplicate = collection duplicate.append(3) pr"
                    },
                    {
                        "question": "Assuming that the following assignment has been successfully executed:  My_list \" [1, 1, 2, 3] Select the expressions which will not raise ",
                        "options": ["A) my_list[-10]", "B) my_list|my_Li1st | 3| I", "C) my list [6]", "D) my_List- [0:1]"],
                        "answer": "B",
                        "explanation": "The code snippet that you have sent is assigning a list of four numbers to a variable called oemy_list . The code is as follows: my_list = [1, 1, 2, 3] The code creates a list object that contains the elements 1, 1, 2, and 3, and assigns it to the va"
                    },
                    {
                        "question": "What is true about tuples? (Select two answers.)",
                        "options": ["A) Tuples are immutable, which means that their contents cannot be changed during their lifetime.", "B) The len { } function cannot be applied to tuples.", "C) An empty tuple is written as { } .", "D) Tuples can be indexed and sliced like lists."],
                        "answer": "A",
                        "explanation": "Tuples are one of the built-in data types in Python that are used to store collections of data. Tuples have some characteristics that distinguish them from other data types, such as lists, sets, and dictionaries. Some of these characteristics are: Tu"
                    },
                    {
                        "question": "Assuming that the following assignment has been successfully executed:  The code is as follows:  the_list = [\"1\", 1, 1, 1] Which of the f",
                        "options": ["A) the_List.index {\"1\"} in the_list", "B) 1.1 in the_list |1:3 |", "C) len (the list [0:2]} <3", "D) the_list. index {'1'} -- 0"],
                        "answer": "C",
                        "explanation": "The code snippet that you have sent is assigning a list of four values to a variable called oethe_list . The code is as follows: the_list = [\"1\", 1, 1, 1] The code creates a list object that contains the values \"1\", 1, 1, and 1, and assigns it to"
                    },
                    {
                        "question": "What is the expected output of the following code?  menu = (\"pizza\": 2.39, \"pasta\": 1.99, \"folpetti\": 3.99)  for value in menu: print",
                        "options": ["A) The code is erroneous and cannot be run.", "B) ppf", "C) 213", "D) pizzapastafolpetti"],
                        "answer": "B",
                        "explanation": "The code snippet that you have sent is using the slicing operation to get parts of a string and concatenate them together. The code is as follows: pizza = oepizza pasta = oepasta folpetti = (folpetti print(pizza[0] + pasta[0] + folpetti[0]) The code "
                    },
                    {
                        "question": "What is the expected result of the following code?  rates = (1.2, 1.4, 1.0) new = rates [3:] for rate in rates [-1:): new += (rate, ) print ",
                        "options": ["A) 5", "B) 2", "C) 1", "D) The code will cause an unhandled"],
                        "answer": "D",
                        "explanation": "The code snippet that you have sent is trying to use a list comprehension to create a new list from an existing list. The code is as follows: my_list = [1, 2, 3, 4, 5] new_list = [x for x in my_list if x > 5] The code starts with creating a list call"
                    },
                    {
                        "question": "What is the expected result of running the following code?",
                        "options": ["A) The code prints 1 .", "C) The code raises an unhandled exception.", "D) The code prints 0"],
                        "answer": "C",
                        "explanation": "The code snippet that you have sent is trying to use the index method to find the position of a value in a list. The code is as follows: the_list = [1, 2, 3, 4, 5] print(the_list.index(6)) The code starts with creating a list called oethe_list that c"
                    },
                    {
                        "question": "What is the expected output of the following code?",
                        "options": ["A) 1", "B) The code raises an unhandled exception.", "C) False", "D) ('Fermi ', '2021', 'False')"],
                        "answer": "D",
                        "explanation": "The code snippet that you have sent is defining and calling a function in Python. The code is as follows: def runner(brand, model, year): return (brand, model, year) print(runner(oeFermi )) The code starts with defining a function called oerunner wit"
                    },
                    {
                        "question": "What is true about exceptions and debugging? (Select two answers.)",
                        "options": ["A) A tool that allows you to precisely trace program execution is called a debugger.", "B) If some Python code is executed without errors, this proves that there are no errors in it.", "C) One try-except block may contain more than one except branch.", "D) The default (anonymous) except branch cannot be the last branch in the try-except block."],
                        "answer": "A",
                        "explanation": "Exceptions and debugging are two important concepts in Python programming that are related to handling and preventing errors. Exceptions are errors that occur when the code cannot be executed properly, such as syntax errors, type errors, index errors"
                    },
                    {
                        "question": "Which of the following are the names of Python passing argument styles? (Select two answers.)",
                        "options": ["A) keyword", "B) reference", "C) indicatory", "D) positional"],
                        "answer": "A",
                        "explanation": "Keyword arguments are arguments that are specified by using the name of the parameter, followed by an equal sign and the value of the argument. For example, print (sep='-', end='!') is a function call with keyword arguments. Keyword arguments can be "
                    },
                    {
                        "question": "What is the expected result of the following code?",
                        "options": ["A) The code is erroneous and cannot be run.", "B) 20", "C) 10"],
                        "answer": "A",
                        "explanation": "The code snippet that you have sent is trying to use the global keyword to access and modify a global variable inside a function. The code is as follows: speed = 10 def velocity(): global speed speed = speed + 10 return speed print(velocity()) The co"
                    },
                ]
            }
        ]