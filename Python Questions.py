#!/usr/bin/env python
# coding: utf-8

# # What is python?

# Python is a versatile, high-level, general-purpose programming language known for its readability and ease of use. It's widely used in web development, data science, machine learning, and software development, among other fields. Python is designed to be interpreted, meaning that code is executed line by line without requiring compilation. 
# 
# Here's a more detailed look: 
# 
# 1. Interpreted: Python is interpreted, so code is executed directly without compilation. 
# 
# 2. High-level: It's considered a high-level language, meaning it's closer to human language than low-level languages. 
# 
# 3. General-purpose: It's not specialized for any particular application but can be used for a wide range of tasks. 
# 
# 4. Object-oriented: Python supports object-oriented programming principles, which helps in organizing code and building complex applications. 
# 
# 5. Readability: Python's syntax is designed to be easy to read and understand. 
# 
# 6. Dynamic typing: Variable types are not explicitly declared in the code, allowing for flexibility. 
# 
# 7. Large standard library: Python comes with a rich set of built-in modules and functions for various tasks. 

# ## Areas where python is being used

# Python is extensively applied in data science, data analysis, machine learning, data engineering, web development, software development, and other fields.

# ## What is high level and low level language?

# High-level languages are designed to be more human-readable and easier to understand, while low-level languages are closer to the machine's instructions and more difficult for humans to understand. High-level languages offer features that simplify programming tasks and are generally platform-independent. Low-level languages, on the other hand, provide more direct control over hardware but require a detailed knowledge of computer architecture. 
# 
# High-Level Languages:
# 
# 1. Human-readable: Designed to be more easily understood by humans than machine language. 
# 
# 2. Abstraction: Abstract away many of the complexities of machine code, making it easier to write and understand. 
# 
# 3. Platform-independent: Can be executed on various platforms with minimal modifications. 
# 
# 4. Easier to debug: Debugging is often straightforward in high-level languages. 
# 
# 5. Examples: Python, Java, C++, JavaScript. 
# 
# Low-Level Languages:
# 
# 1. Machine-friendly: Closer to the machine's instructions and easier for the machine to interpret.
# 
# 2. Machine-dependent: Often tied to a specific hardware architecture. 
# 
# 3. More efficient: Can produce more efficient code through optimization for a specific system architecture. 
# 
# 4. Direct control: Provide more direct control over hardware and resources. 
# 
# 5. Examples: Assembly language, machine language. 

# ## What is interpreted language?

# An interpreted language is a type of programming language where the code is executed directly, line by line, without being compiled into machine code beforehand. Instead of a compiler translating the entire program, an interpreter reads and executes each instruction as it's encountered. 

# Here's a more detailed explanation:
# 
# 1. No Compilation:
# Unlike compiled languages (like C++ or Java), interpreted languages don't require a separate compilation step where the entire program is converted into machine code. 
# 
# 2. Line-by-Line Execution:
# The interpreter reads the source code and executes each line of code one at a time, interpreting it as it goes. 
# 
# 3. Interpreter Required:
# To run an interpreted language program, you need an interpreter, which is a program that reads and executes the source code. 
# 
# 4. Examples:
# Popular interpreted languages include Python, JavaScript, Ruby, Perl, and PHP. 

# ## What is compiled language?

# A compiled language is a programming language where source code is translated into machine code or intermediate code (like bytecode) by a compiler before it is executed. This translation happens before runtime, resulting in an executable file that can be run directly by the computer's CPU or a virtual machine. 
# 
# 
# Key characteristics of compiled languages:
# 
# 1. Pre-runtime translation:
# The entire source code is translated into machine code (or an intermediate representation like bytecode) by a compiler before the program is executed. 
# 
# 2. Executable file:
# The output of the compilation process is an executable file, like a .exe file on Windows, which can be directly run by the operating system. 
# 
# 3. Potentially faster execution:
# Since the translation is done upfront, the execution of the program can be faster, as there's no need to translate the code at runtime, says FreeCodeCamp. 
# 
# 4. Platform-dependent (generally):
# Compiled languages often result in machine code that is specific to the architecture of the target platform. A program compiled on one system might not work on another system with a different CPU architecture, explains Naukri Code 360. 

# Examples of compiled languages:
# 
# C, C++, C#
# 
# Fortran
# 
# Pascal
# 
# COBOL 

# ## What is statically typed language?

# A statically typed language is one where the data type of a variable is known at compile time, meaning before the code is executed. This type information must be explicitly declared by the programmer, or in some cases, inferred by the compiler. Examples include C, C++, Java, and Pascal. 

# ## what is dynamically typed language

# A dynamically typed language is a programming language where type checking is done at runtime rather than at compile time. This means that you don’t have to explicitly declare variable types—the language figures it out while the program is running.
# 
# Key Characteristics:
# 
# 1. No type declarations required: You can assign any type of value to a variable without specifying the type.
# 
# 2. Flexible variable usage: A variable can be reassigned to different types over its lifetime.
# 
# 3. Type errors at runtime: If you perform invalid operations (like adding a string to an integer), the error will be detected only when that line is executed.

# In[3]:


#Example in Python (a dynamically typed language):
x = 10        # x is an integer
x = "hello"   # now x is a string
x


# #Common Dynamically Typed Languages:
#     
# 1. Python
# 
# 2. JavaScript
# 
# 3. Ruby
# 
# 4. PHP
# 
# 5. Perl

# ## what is weekly typed language

# A weakly typed language is a programming language that does not strictly enforce data types during compilation or runtime. It allows for implicit type conversions, meaning that the language can automatically convert a value from one type to another if the context suggests it, according to Medium. In essence, variables don't need to be explicitly declared with a specific type, and the language handles type conversions as needed during operations. 
# 

# ## what is strongly typed language

#  A strongly typed language enforces strict type checking, meaning the compiler or interpreter will flag an error if an operation is attempted on incompatible data types. In essence, it ensures that variable types are known and consistent throughout the program's execution, helping to prevent errors at runtime. 

# ## what is  .PYC  File (byte code)?

# pyc files are compiled bytecode files that are generated by the Python interpreter when a Python script is imported or executed. The . pyc files contain compiled bytecode that can be executed directly by the interpreter, without the need to recompile the source code every time the script is run.

# What is a .pyc File?
# 
# .pyc stands for Python Compiled.
# 
# It is generated automatically by Python when a .py script is run.
# 
# The file contains bytecode, which is a lower-level, platform-independent representation of the code.
# 
# Bytecode is what the Python interpreter (specifically the CPython VM) executes.

# ## what is  PVM?

# PVM (Parallel Virtual Machine) is a software system that allows a collection of heterogeneous computers to be treated as a single, powerful parallel computer. It essentially creates a "virtual machine" where different types of computers can work together on the same task. This virtual machine can consist of workstations, multiprocessors, supercomputers, and PCs, all connected over a network. 

# ## how python internally works?

# 1. Code Editor: Code Editor is the first stage of programs where we write our source code. This is human-readable code written according to Python’s syntax rules. It is where the execution of the program starts first.
# 
# 2. Source code: The code written by a programmer in the code editor is then saved as a .py file in a system. This file of Python is written in human-readable language that contains the instructions for the computer.
# 
# 3. Compilation Stage: The compilation stage of Python is different from any other programming language. Rather than compiling a source code directly into machine code. python compiles a source code into a byte code. In the compilation stage python compiler also checks for syntax errors. after checking all the syntax errors, if no such error is found then it generates a .pyc file that contains bytecode.
# 
# 4. Python Virtual Machine(PVM): The bytecode then goes into the main part of the conversion is the Python Virtual Machine(PVM). The PVM is the main runtime engine of Python. It is an interpreter that reads and executes the bytecode file, line by line. Here In the Python Virtual Machine translate the byte code into machine code which is the binary language consisting of 0s and 1s. The machine code is highly optimized for the machine it is running on. This binary language is only understandable by the CPU of a system.
# 
# 5. Running Program: At last, the CPU executes the given machine code and the main outcome of the program comes as performing task and computation you scripted at the beginning of the stage in your code editor.
#Component	               Role

1. Tokenizer (Lexer)	  Converts code to tokens

2. Parser	             Builds AST from tokens

3. Compiler	             Turns AST into bytecode

4. Interpreter (PVM)	 Executes bytecode line-by-line

5. Memory Manager   	 Handles object allocation & garbage collectionYour Code (.py)
   ↓
Tokenization
   ↓
Parsing → Abstract Syntax Tree (AST)
   ↓
Compilation → Bytecode (.pyc)
   ↓
Execution → Python Virtual Machine (PVM)

# ## What is PEP8?

# PEP 8 is the official style guide for Python code, providing guidelines for writing readable and consistent code. It focuses on code layout, formatting, and naming conventions to improve code quality and readability. Adhering to PEP 8 makes your code easier to understand, maintain, and collaborate on. 

# ## What is PIP and What is use of PIP?

# pip (also known by Python 3's alias pip3) is a package-management system written in Python and is used to install and manage software packages. The Python Software Foundation recommends using pip for installing Python applications and its dependencies during deployment.

# ## What is byte code and when it is created?

# Bytecode is an intermediate, platform-independent code generated by a compiler during the compilation of source code. It's not directly executable by the CPU but is interpreted by a virtual machine (VM) which then translates it into machine-executable instructions for the specific platform. 

# ## What is indentation  in python ? Does python rely on indentation?

#  Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

# Indentation refers to the whitespace (spaces or tabs) used at the beginning of a line of code to define the structure and hierarchy of the program. It’s used to indicate which statements are part of the same block (such as loops, functions, and conditionals).

# ## what is variable in python?

# A variable in Python serves as a named storage location in the computer's memory, used to hold data values. It allows programs to store, retrieve, and manipulate information during execution. Unlike some other programming languages, Python doesn't require explicit declaration of a variable's data type; it dynamically infers the type based on the assigned value.
# When naming variables in Python, certain rules should be followed: 
#     
# 1. Variable names can consist of letters, digits, and underscores.
# 
# 2. They cannot begin with a digit.
# 
# 3. Variable names are case-sensitive (myVar and myvar are considered different).
# 
# 4. Avoid using Python keywords (e.g., if, else, for) as variable names.
# Examples of variable assignment
name = "Alice"  # String data type
age = 30        # Integer data type
height = 5.8    # Float data type
is_active = True # Boolean data type

# Demonstrating dynamic typing
x = 10      # x is an integer
x = "Hello" # x is now a string
# ## what are variable naming rules in python?

# Here are the rules for naming variables in Python: 
#     
# 1. Variable names must begin with a letter (a-z, A-Z) or an underscore (_).
# 
# 2. The rest of the variable name can consist of letters, numbers (0-9), and underscores.
# 
# 3. Variable names are case-sensitive (e.g., myVariable, myvariable, and MyVariable are all distinct).
# 
# 4. Reserved keywords in Python (e.g., if, else, for, while, def, class, import, True, False, None, etc.) cannot be used as variable names.
# 
# 5. Variable names cannot contain spaces or special characters other than the underscore.

# ## what is datatype and name of types in python?

# A datatype in Python refers to the kind of value that a variable or an object can hold. It defines what operations can be performed on the value and how it is stored in memory.
# 
# Python is a dynamically typed language, meaning you don't need to specify the type of a variable when declaring it; Python automatically determines the type during runtime.

Data Types	Examples	Explanation	Mutable/Immutable?

Strings	"Hello!", "23.34"	Text - anything between

" "  becomes string	Immutable

Integers	5364	Whole numbers	Immutable

Floats	3.1415	Decimal Numbers	Immutable

Booleans	True, False	Truth values that represent Yes/No	Immutable

Lists	[1,2,3,4,5]	A collection of data,

sits between  [ ]  	Mutable

Tuples	(1,2,3,4,5)	A collection of data,

sits between  ( )  	Immutable

Dictionaries	{"a":1, "b":2, "c":3}	A collection of data,

sits between  { }  	Mutable
# ## what is keyword in python?

# Keywords in Python are reserved words that have predefined meanings and purposes within the language. These keywords cannot be used as identifiers (variable names, function names, etc.) because they are an integral part of Python's syntax and structure. Each keyword performs a specific task, defining the flow and logic of a Python program.

# Here's a list of common Python keywords:
# 
# and, or, not: Logical operators.
# 
# if, elif, else: Conditional statements.
# 
# for, while: Looping constructs.
# 
# break, continue: Loop control statements.
# 
# def: Function definition.
# 
# class: Class definition.
# 
# return: Exit a function and return a value.
# 
# try, except, finally: Exception handling.
# 
# import, from, as: Module import statements.
# 
# is: Check object identity.
# 
# in: Check membership in a sequence.
# 
# lambda: Anonymous function definition.
# 
# pass: Null statement (placeholder).
# 
# global, nonlocal: Variable scope modifiers.
# 
# assert: Debugging aid.
# 
# with: Context management.
# 
# yield: Generator function.
# 
# async, await: Asynchronous programming.
# 
# True, False: Boolean values.
# 
# None: Represents the absence of a value.

# Keywords are case-sensitive and must be used exactly as defined. They are fundamental to writing correct and understandable Python code, guiding the interpreter in executing instructions.

# In[ ]:





# In[ ]:





# In[ ]:




