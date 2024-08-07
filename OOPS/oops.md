
# Object-Oriented Programming (OOP) in Python

## Introduction

Object-Oriented Programming (OOP) is a way of organizing code using objects and classes. This makes the code easier to understand and manage.

## OOP Concepts

1. **Class and Object**
2. **Encapsulation**
3. **Inheritance**
4. **Polymorphism**
5. **Abstraction**

### 1. Class and Object

A class is like a blueprint for creating objects. An object is an instance of a class.

#### Example

```python
# Define a class named 'Person'
class Person:
    # Constructor method to initialize the class attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method to display person's information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object of the Person class
person1 = Person("Alice", 30)
person1.display_info()  # Output: Name: Alice, Age: 30
```

### 2. Encapsulation

Encapsulation means keeping some data private, so it cannot be accessed directly from outside the class.

#### Example

```python
# Define a class named 'Counter'
class Counter:
    # Constructor method to initialize the class attribute
    def __init__(self):
        self.__count = 0  # Private attribute
    
    # Method to increment the count
    def increment(self):
        self.__count += 1
    
    # Method to get the current count
    def get_count(self):
        return self.__count

# Create an object of the Counter class
counter = Counter()
counter.increment()
counter.increment()
print(counter.get_count())  # Output: 2
```

### 3. Inheritance

Inheritance means creating a new class based on an existing class. The new class (child) inherits attributes and methods from the existing class (parent).

#### Example

```python
# Define a base class named 'Animal'
class Animal:
    # Method to initialize the class attribute
    def __init__(self, name):
        self.name = name

# Define a derived class named 'Dog' that inherits from 'Animal'
class Dog(Animal):
    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object of the Dog class
dog = Dog("Buddy")
dog.bark()  # Output: Buddy says Woof!
```

### 4. Polymorphism

Polymorphism means using the same method name for different objects, and each object responds in its own way.

#### Example

```python
# Define a class named 'Cat'
class Cat:
    # Method to make the cat sound
    def sound(self):
        print("Meow")

# Define a class named 'Cow'
class Cow:
    # Method to make the cow sound
    def sound(self):
        print("Moo")

# Function to call the sound method of any animal
def make_sound(animal):
    animal.sound()

# Create objects of Cat and Cow classes
cat = Cat()
cow = Cow()

make_sound(cat)  # Output: Meow
make_sound(cow)  # Output: Moo
```

### 5. Abstraction

Abstraction means showing only the necessary details and hiding the complex implementation.

#### Example

```python
from abc import ABC, abstractmethod

# Define an abstract base class named 'Shape'
class Shape(ABC):
    # Abstract method to be implemented in derived classes
    @abstractmethod
    def area(self):
        pass

# Define a derived class named 'Rectangle' that inherits from 'Shape'
class Rectangle(Shape):
    # Method to initialize the class attributes
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Method to calculate the area of the rectangle
    def area(self):
        return self.width * self.height

# Create an object of the Rectangle class
rectangle = Rectangle(4, 5)
print(rectangle.area())  # Output: 20
```

## Conclusion

OOP in Python helps in creating clear and efficient code. By using classes and objects, encapsulation, inheritance, polymorphism, and abstraction, developers can create code that is easy to manage and extend.

