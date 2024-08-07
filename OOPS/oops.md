# Object-Oriented Programming (OOP) in Python

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to organize code. It allows for the creation of reusable and modular code, making it easier to manage and maintain large codebases.

## OOP Concepts

1. **Class and Object**
2. **Encapsulation**
3. **Inheritance**
4. **Polymorphism**
5. **Abstraction**

### 1. Class and Object

A class is a blueprint for creating objects (a particular data structure). An object is an instance of a class.

#### Example

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Create an object of the Car class
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
```

### 2. Encapsulation

Encapsulation is the process of wrapping data and methods into a single unit (class) and restricting access to some of the object's components.

#### Example

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

# Create an object of the BankAccount class
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())
```

### 3. Inheritance

Inheritance is the mechanism by which one class can inherit the attributes and methods of another class.

#### Example

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create objects of Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())
```

### 4. Polymorphism

Polymorphism allows methods to do different things based on the object it is acting upon, even if the method calls are the same.

#### Example

```python
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Create objects of Square and Circle classes
square = Square(4)
circle = Circle(3)
print(f"Area of square: {square.area()}")
print(f"Area of circle: {circle.area()}")
```

### 5. Abstraction

Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object.

#### Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    
    def stop_engine(self):
        print("Car engine stopped")

# Create an object of the Car class
my_car = Car()
my_car.start_engine()
my_car.stop_engine()
```

## Conclusion

OOP in Python provides a clear and efficient way to structure code. By using classes and objects, encapsulation, inheritance, polymorphism, and abstraction, developers can create modular, reusable, and maintainable code.

