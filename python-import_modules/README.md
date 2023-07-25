## Python - import & modules

1. **Why Python programming is awesome**: Python is awesome due to its simplicity, readability, versatility, large community support, and extensive libraries that make it easy to accomplish various tasks.

2. **How to import functions from another file**: To import functions from another file in Python, use the `import` statement followed by the module or file name without the file extension. Example: `import my_module`.

3. **How to use imported functions**: After importing a module, you can use its functions by referencing them using dot notation. Example: `my_module.my_function()`.

4. **How to create a module**: A module in Python is simply a file containing Python code. To create a module, write your functions and code in a .py file with a descriptive name.

5. **How to use the built-in function dir()**: The `dir()` function is used to list all the names in the current scope or the attributes of an object. It helps explore the available functions and methods.

6. **How to prevent code in your script from being executed when imported**: By using the `if __name__ == "__main__":` condition, you can ensure that certain code only runs when the script is executed directly and not when imported as a module.

7. **How to use command line arguments with your Python programs**: You can use the `sys.argv` list from the `sys` module to access command-line arguments passed to a Python script.

8. **What’s the difference between errors and exceptions**: Errors are issues that occur during program execution that can lead to the program's termination. Exceptions are a type of error that can be caught and handled, allowing the program to continue running.

9. **What are exceptions and how to use them**: Exceptions are raised when an error occurs during program execution. To use them, you can use a `try` block to enclose the code that might raise an exception and handle it using `except` blocks.

10. **When do we need to use exceptions**: Exceptions are useful when handling exceptional cases or errors in a program's execution, allowing graceful error handling instead of abrupt termination.

11. **How to correctly handle an exception**: To handle exceptions, use a `try-except` block. Place the potentially problematic code in the `try` block, and in the `except` block, specify what to do if an exception is raised.

12. **What’s the purpose of catching exceptions**: The purpose of catching exceptions is to prevent a program from crashing due to errors and allow developers to handle these errors gracefully, ensuring the program continues running.

13. **How to raise a built-in exception**: You can raise a built-in exception using the `raise` keyword followed by the exception type. Example: `raise ValueError("Invalid input")`.

14. **When do we need to implement a clean-up action after an exception**: In situations where resources like files or connections are opened, it's essential to implement clean-up actions using `finally` block to ensure they are properly closed, regardless of whether an exception occurs.
