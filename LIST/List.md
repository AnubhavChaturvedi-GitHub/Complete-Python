### List Creation
```python
my_list = [1, 2, 3, 4, 5]  # Creating a list
```

### Accessing Elements
```python
element = my_list[0]  # Accessing the first element
```

### Slicing
```python
sub_list = my_list[1:4]  # Slicing a list from index 1 to 3
```

### Adding Elements
```python
my_list.append(6)        # Adding an element at the end
my_list.insert(2, 10)    # Inserting an element at index 2
```

### Removing Elements
```python
my_list.remove(3)        # Removing the first occurrence of 3
element = my_list.pop()  # Removing and returning the last element
element = my_list.pop(1) # Removing and returning the element at index 1
del my_list[0]           # Deleting the element at index 0
```

### List Operations
```python
length = len(my_list)              # Getting the length of the list
index = my_list.index(10)          # Finding the index of the first occurrence of 10
count = my_list.count(10)          # Counting the occurrences of 10 in the list
my_list.reverse()                  # Reversing the list
my_list.sort()                     # Sorting the list in ascending order
my_list.sort(reverse=True)         # Sorting the list in descending order
new_list = my_list.copy()          # Creating a shallow copy of the list
my_list.clear()                    # Clearing all elements from the list
```

### List Comprehensions
```python
squared = [x**2 for x in my_list]  # Creating a new list with squared elements
```

### Concatenation and Repetition
```python
combined_list = my_list + [6, 7, 8]    # Concatenating lists
repeated_list = my_list * 3            # Repeating elements
```

### Iterating Through a List
```python
for element in my_list:
    print(element)
```

### Membership Test
```python
if 10 in my_list:
    print("10 is in the list")
```

### Advanced List Operations

#### Nested Lists
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = nested_list[0][1]  # Accessing element 2 from the first list
```

#### List Methods
```python
# Extend the list by appending all elements from another list
my_list.extend([6, 7, 8])

# Creating a list with repeated elements
repeated_list = [0] * 5  # [0, 0, 0, 0, 0]

# Creating a list from a string
char_list = list("hello")  # ['h', 'e', 'l', 'l', 'o']
```

#### List Iteration with Index
```python
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
```

### List Functions

#### `map` Function
```python
squared = list(map(lambda x: x**2, my_list))  # Applying a function to all elements
```

#### `filter` Function
```python
even_numbers = list(filter(lambda x: x % 2 == 0, my_list))  # Filtering elements based on a condition
```

#### `reduce` Function (from functools module)
```python
from functools import reduce
sum_all = reduce(lambda x, y: x + y, my_list)  # Reducing the list to a single value
```

### Advanced List Comprehensions
```python
# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]  # Creating a 3x3 multiplication table
```

### List Manipulation with `zip`
```python
# Combining two lists element-wise
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list(zip(list1, list2))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### List Unpacking
```python
# Unpacking a list into variables
a, b, c = [1, 2, 3]
```

### List Flattening
```python
# Flattening a list of lists
flat_list = [item for sublist in nested_list for item in sublist]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


