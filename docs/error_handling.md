# Error Handling

## Introduction

Error handling is a way to deal with errors that might occur in your code. It is a way to prevent your program from crashing when an error occurs.  It allows your program to recognise that something has gone wrong and respond to it in a way that you define.  This can be particularly useful when you are working with user input, as you can anticipate that the user might enter something unexpected.  It is also useful when working with network connections or files that might not be available.  In this section, we will look at how to use error handling in Python.

## Syntax

The syntax for error handling in Python is as follows:

```python
try:
    # code that might raise an error
except ErrorType:
    # code to run if an error of type ErrorType occurs
```

The `try` block contains the code that might raise an error.  If an error occurs, the program will jump to the `except` block.  The `except` block contains the code that should run if an error occurs.  The `ErrorType` is the type of error that you are expecting.  You can specify the type of error that you are expecting, or you can use a general `except` block to catch any error.

## Example

In the following example, we will try to open a file that does not exist.  We will use error handling to catch the error that occurs when the file does not exist.

```python
try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("File not found")
```

In this example, we try to open a file called `file.txt` in read mode.  If the file does not exist, a `FileNotFoundError` will be raised.  We use error handling to catch this error and print a message to the console.

---

## Different Error Types

Python has a number of built-in error types that you can use to catch specific errors.  Some of the most common error types are:

- `FileNotFoundError`: Raised when a file is not found
- `TypeError`: Raised when an operation is performed on an object of an inappropriate type
- `ValueError`: Raised when a function receives an argument of the correct type, but with an inappropriate value
- `ZeroDivisionError`: Raised when division or modulo by zero is performed
- `IndexError`: Raised when an index is out of range
- `KeyError`: Raised when a key is not found in a dictionary
- `NameError`: Raised when a local or global name is not found
- `SyntaxError`: Raised when there is a syntax error in the code
- `IndentationError`: Raised when there is an incorrect indentation in the code
- `AttributeError`: Raised when an attribute reference or assignment fails
- `ImportError`: Raised when an import statement fails
- `ModuleNotFoundError`: Raised when a module is not found

You can use these error types to catch specific errors in your code and catch different types from the same `try` block.

For example, you can catch a `FileNotFoundError` and a `ValueError` in the same `try` block:

```python
try:
    file = open("file.txt", "r")
    value = int("abc")
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid value")
```

In this example, we try to open a file called `file.txt` in read mode and convert the string `"abc"` to an integer.  If the file does not exist, a `FileNotFoundError` will be raised.  If the string cannot be converted to an integer, a `ValueError` will be raised.  We use error handling to catch these errors and print a message to the console.

---

## The `finally` Block

You can use a `finally` block to run code that should always run, regardless of whether an error occurs.  The `finally` block is optional and is placed after the `except` block.

```python
try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")
    file.close()
```

In this example, we try to open a file called `file.txt` in read mode.  If the file does not exist, a `FileNotFoundError` will be raised.  We use error handling to catch this error and print a message to the console.  We then use a `finally` block to close the file, regardless of whether an error occurs.

`try:except` can also be used within a ***context manager***:

```python
with open("file.txt", "r") as file:
    try:
        # code that might raise an error
    except ErrorType:
        # code to run if an error of type ErrorType occurs
```

In this case, the `finally` block is not needed, as the file will be closed automatically when the `with` block exits.
