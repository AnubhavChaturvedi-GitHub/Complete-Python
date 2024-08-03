# Python Basics

## 1. Comments

Comments in Python are used to explain code and make it more readable. There are two types of comments:

- **Single-Line Comments**: Start with a `#`.
- **Multi-Line Comments**: Enclosed in triple quotes `'''` or `"""`.

```python
# This is a single-line comment

'''
This is a 
multi-line comment
'''
```

## 2. Variables

Variables are used to store data. You don't need to declare the data type explicitly.

```python
x = 5           # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True # Boolean

print(x)        # Output: 5
print(y)        # Output: 3.14
print(name)     # Output: Alice
print(is_active) # Output: True
```

## 3. Data Types

Python has several built-in data types:

- **Integer**: Whole numbers.
- **Float**: Decimal numbers.
- **String**: Text.
- **Boolean**: `True` or `False`.

```python
age = 30                  # int
height = 5.9              # float
greeting = "Hello, World!" # str
is_student = False        # bool

print(type(age))          # Output: <class 'int'>
print(type(height))      # Output: <class 'float'>
print(type(greeting))    # Output: <class 'str'>
print(type(is_student))  # Output: <class 'bool'>
```

## 4. Operators

Operators are used to perform operations on variables and values.

- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`, `**`, `//`
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `and`, `or`, `not`

```python
a = 10
b = 5

print(a + b)   # Output: 15
print(a - b)   # Output: 5
print(a * b)   # Output: 50
print(a / b)   # Output: 2.0
print(a % b)   # Output: 0
print(a ** b)  # Output: 100000
print(a // b)  # Output: 2

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

print(a > 5 and b < 10)  # Output: True
print(a > 5 or b > 10)   # Output: True
print(not(a > 5))        # Output: False
```

## 5. Conditional Statements

Conditional statements allow you to execute code based on certain conditions.

```python
x = 20

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is 10")
else:
    print("x is less than 10")

# Output: x is greater than 10
```

## 6. Loops

Loops are used to execute a block of code repeatedly.

- **For Loop**: Iterates over a sequence (list, tuple, string, etc.).
- **While Loop**: Repeats as long as a condition is true.

```python
# For Loop
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
```

## 7. Functions

Functions are used to encapsulate code into reusable blocks.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Output: Hello, Alice!
```

## 8. Classes

Classes are used to create user-defined objects. They encapsulate data and functions.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
print(person1.greet())

# Output: Hello, my name is Alice and I am 30 years old.
```

---

Feel free to vist [NetHyTech](https://www.youtube.com/@nethytech)
