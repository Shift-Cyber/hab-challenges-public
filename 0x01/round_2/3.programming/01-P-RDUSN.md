# Buckets - 75pts
### 01-P-RDUSN
*Author: Nate Singer (Helix)*

Programming is the process of creating instructions for a computer to follow using a specific language. These instructions, called code, tell the computer what to do, like creating a game or displaying information on a website. There are many different programming languages, each with their own rules and syntax. Once the code is written, it needs to be run or executed so the computer can follow the instructions. Programming is used in many fields and is a powerful tool to automate tasks, solve problems, and create new things.

## Teaching Points
1. How can we read files?
2. How do we create variables?

## Challenge Prompt
**NON-STANDARD FLAG FORMAT**

Grab the data file and add up all the times danny and elise appear. Multiple those two numbers together, that is your challenge answer.

For example, take this sample prompt, the answer is 24: ```6 * 4 = 24```
```
danny
charlie
danny
billy
danny
elise
charlie
billy
elise
charlie
alice
danny
billy
danny
danny
elise
charlie
elise
charlie
alice
```

## Solution Guide
*See the solution files in the resources directory.*

## Reference Material
We are going to use Python as the core language for teaching programming. The concepts will translate to other languages but using python as a base learning tool keepds things simple and allows for easy translation to exploitation down the line.

### What is Python?
Python is a programming language that is used to write computer programs. It's called a "high-level" language because it is easy for humans to read and write, and it is also easy for computers to understand and execute. With Python, you can create all sorts of programs, from simple scripts to full-fledged applications. It's a popular choice for beginners because it is relatively easy to learn, and it is also widely used in industry, which means that there are many resources and libraries available to help you accomplish different tasks.

### How can we read files?
To read a file, you first need to know the location of the file on your computer, known as the file path. Once you have the file path, you can use the built-in "open" function in Python to open the file. The open function returns a "file object" which you can use to read the contents of the file.

Here's an example of how to read a file called "example.txt" in the same directory as your Python script:
```
# Open the file
file = open("example.txt", "r")

# Read the contents of the file
contents = file.read()

# Print the contents of the file
print(contents)

# Close the file
file.close()
```

You can also use a with statement to open the file, it will automatically close the file after done with it
```
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
```

This code will open the file "example.txt" in "read" mode, which means that you can only read the contents of the file and not make any changes to it. The read() function reads the entire contents of the file and returns it as a string. The print(contents) will output the contents of the file to the console.

### How can we store and use data through variables?
A variable in Python is like a container that can hold a value or piece of data. You can give the variable a name and then use that name to refer to the value stored inside of it.

For example, you can create a variable called "x" and give it the value of 5 like this:
```
x = 5
```

Now, whenever you use the variable "x" in your code, it will refer to the value 5. You can also change the value of a variable after it has been created.
```
x = 5
x = x + 3
print(x) # output: 8
```

You can also use variables to store different types of data, such as strings or lists. For example:
```
name = "John"
age = 15
fruits = ["apple","banana","orange"]
```

You can also use variables in mathematical operations:
```
x = 5
y = 3
result = x + y
print(result) # output: 8
```

Also, you can use variables to store results of function calls or other operations.
```
result = len("hello")
print(result) #output: 5
```

In summary, variables are like named containers that can hold values or data. You can give them a name, assign a value to them, and then use them in your code to refer to that value.

### External References
- https://realpython.com/working-with-files-in-python/
- https://realpython.com/python-variables/
