# Blobs - 75pts
### 01-P-BC6VD
*Author: Nate Singer (Helix)*

Programming is the process of creating instructions for a computer to follow using a specific language. These instructions, called code, tell the computer what to do, like creating a game or displaying information on a website. There are many different programming languages, each with their own rules and syntax. Once the code is written, it needs to be run or executed so the computer can follow the instructions. Programming is used in many fields and is a powerful tool to automate tasks, solve problems, and create new things.

## Teaching Points
1. What is a data type?
2. Why do data types matter?
3. How can we do basic arithmetic in Python?

## Challenge Prompt
Hey there navigator, its time to follow some directions. Take your challenge input (file) and start at the initial position, such as the below x=52, y=-31. Just like you are on a 2d graph, move in the direction the arrows tell you to. In the below example you end up in the same x position for a difference of 0 and down one for a y difference of -1. Take your final position, in this case 52, -32 and multiply the values together--that is your final position. The answer to the sample prompt is -1664.

```
(52,-31)

↘ ↙ ↘ ↙ ↘ → ← ↖ ← ↗ ↘ ↑ ↑ ↓ ↗ ← → ↙ ↖ ↑ 
```

## Solution Guide
*See the reference material and solution file in resources, generally write a case processor.*

## Reference Material
### Variable Types
In Python, there are different types of variables that can hold different types of data.

- int stands for integer, which is a whole number like 1, 2, or 3.
- float stands for floating-point number, which is a number with a decimal point like 3.14 or 2.718.
- str stands for string, which is a sequence of characters like "hello" or "goodbye".
- bool stands for boolean, which can only have two possible values: True or False
- list is a list of items which are enclosed in square brackets [], the items inside list can be of any data type, and the values inside the list are separated by commas.
- tuple is similar to list, but the items inside a tuple are enclosed in parentheses (). Also, tuples are immutable, which means you can't change the values of tuple items after it was created.
- dict stands for dictionary, which is a collection of key-value pairs. Each key is associated with a value, and you can use the key to access the value.

Here are some examples of how to create variables of different types:
```
x = 5 # integer
y = 2.718 # float
name = "John" # string
is_happy = True # boolean
fruits = ["apple", "banana", "orange"] # list
person = ("John", 25, "Student") # tuple
person_data = {'name': 'John', 'age': 25, 'occupation': 'Student'} # dictionary
```

It is important to use the correct variable type for the data you are working with. For example, you wouldn't want to use a string variable to store a number because it would cause errors in your code.

Also, Python is a dynamically typed language, which means that you don't need to specify the type of a variable when you create it. Python will automatically determine the type based on the value you assign to it.

### Loops
There are two basic types of loops in Python: for loops and while loops.

A for loop is used to iterate over a sequence of items, such as a list, tuple, or string. The general syntax for a for loop is:

```
for variable in sequence:
    # code to execute
```

For example, you can use a for loop to iterate over a list of numbers and print each one:
```
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

A while loop is used to repeatedly execute a block of code as long as a certain condition is true. The general syntax for a while loop is:
```
while condition:
    # code to execute
```

For example, you can use a while loop to repeatedly ask the user for input until they enter the correct password:
```
password = "secret"
while True:
    user_input = input("Enter your password: ")
    if user_input == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Please try again.")
```

In this example, the while loop will continue to run as long as the value of the variable user_input is not equal to the value of the variable password. When the user enters the correct password, the loop will break, and the program will continue to execute the next line of code.

It's important to use the correct type of loop and also to include a way to exit the loop, otherwise, the loop will run indefinitely and cause an infinite loop.


### Itteration over Lines in a File
In Python, you can iterate over the lines of a file using a for loop. The for loop can be used to go through each line of the file, one at a time. Here is an example of how you can iterate over the lines of a file called "example.txt":

```
# open the file in read mode
with open('example.txt', 'r') as file:
    # use a for loop to iterate over the lines
    for line in file:
        # print each line
        print(line)
```

### Basic Arithmetic in Python
Python can be used to perform basic arithmetic operations, such as addition, subtraction, multiplication, and division.

+ operator is used for addition, for example:
```
x = 5
y = 3
result = x + y
print(result) # output: 8
```

- operator is used for subtraction, for example:
```
x = 5
y = 3
result = x - y
print(result) # output: 2
```

* operator is used for multiplication, for example:
```
x = 5
y = 3
result = x * y
print(result) # output: 15
```

/ operator is used for division, for example:
```
x = 5
y = 3
result = x / y
print(result) # output: 1.6666667
```

% operator is used for modulo, which gives the remainder of a division, for example:
```
x = 5
y = 3
result = x % y
print(result) # output: 2
```

** operator is used for exponentiation, for example:
```
x = 5
y = 3
result = x ** y
print(result) # output: 125
```

You can also use parentheses to group expressions and force a certain order of operations. For example:

```
x = 5
y = 3
result = (x + y) * 2
print(result) # output: 16
```

In this example, (x + y) is evaluated first, and then the result is multiplied by 2.

And also you can use python's built-in functions like round(), abs(), pow() etc.

```
x = 5.678
result = round(x, 2)
print(result) # output: 5.68
```

```
x = -5
result = abs(x)
print(result) # output: 5
```

```
x = 5
y = 3
result = pow(x, y)
print(result) # output: 125
```

These are the basic arithmetic operations that you can perform in Python, you can use these operations to perform calculations and solve problems in your program.


### External References
- https://www.programiz.com/python-programming/variables-datatypes
