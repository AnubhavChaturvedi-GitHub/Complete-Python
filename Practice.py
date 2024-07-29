# Creating the list
list1 = ["shejal", 1, True]
print(list1)

# Find the type
list2 = ["shejal", 1, True]
print(type(list2))

# Multi-dimensional list
List3 = [[1, 2, 3], [5, 6, 7]]
print(List3)
print(type(List3))

# Print specific elements in the list
List4 = [1, 2, 4, 5, 7, 8]
print(List4)
print(List4[3])  # Indexing starts from 0

# Negative indexing
print(List4[5])
print(List4[-1])

# Find the number of elements in the list
print(len(List4))

# Reverse the list
list6 = List4.copy()
list6.reverse()
print(list6)

# Clear the list
list6.clear()
print(list6)

# Add an element in the list
list6 = [1, 2, 3]
list6.append(4)
print(list6)

# Add in specific position
list6.insert(-1, 8)
print(list6)

# Slicing in list
lsis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lsis[1:5])

# Print all the elements in the list
for i in lsis:
    print(i)

# Check if an element is present in the list
x = 10
if x in lsis:
    print("Element is present in lsis")
else:
    print("Element is not present")

# Remove an element from the list
list_new = [1, 2, 3, 4, 5]
print(len(list_new))
print(list_new)
list_new.remove(3)
print(len(list_new))
print(list_new)

# Pop the last element
list_new = [1, 2, 3, 4, 5]
list_new.pop()
print(list_new)
list_new.pop(2)
print(list_new)

# Delete an element by index
list_new1 = [1, 2, 3, 4, 5]
del list_new1[0]
print(list_new1)

# Find the index of an element
x = ["hello", "hii", "how are you", "bye"]
print(x.index("bye"))

# Count specific elements in the list
x = [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(x.count(1))

# Sorting the list
x = [1, 5, 9, 4, 6, 7, 3, 8]
x.sort()
print(x)
print(sorted(x))

# Sort the list in reverse
x.sort(reverse=True)
print(x)
x = sorted(x)
x.reverse()
print(x)

# Reverse the list
x = [1, 5, 9, 4, 6, 7, 3, 8]
x.reverse()
print(x)

# Square each element
x = [1, 5, 9, 4, 6, 7, 3, 8]
c = []
for i in x:
    new_e = i**2
    c.append(new_e)
print(c)

# Second method to square each element
my_list = [i**2 for i in x]
print(my_list)

# Concatenate two lists
a = [1, 2]
b = [2, 3]
c = a + b
print(c)

# Second loop method to concatenate lists
for i in b:
    a.append(i)
print(a)

# Append multiple elements to a list
x = [1, 2]
c = [8, 5, 8, 5, 8]
for i in c:
    x.append(i)
print(x)
x.extend([1, 2, 3, 4, 5, 65, 4, 6, 4])
print(x)

# Create your own extend method
def extend_new(c, list1):
    for i in list1:
        c.append(i)
    return c

def extend_new1(c, list1):
    return c + list1

c = [8, 5, 8, 5, 8]
extend_new(c, [1, 2, 3, 4, 5])
print(c)
extend_new1(c, [1, 2, 3, 4, 5])
print(c)

# Repeated list
x = [1, 2]
y = x * 3
print(y)

# Zip method
x = [1, 2, 3]
y = ["hello", "hi", "bye"]
z = list(zip(x, y))
print(z)
z = dict(zip(x, y))
print(z)

# String to list
z = "she jal"
y = list(z)
print(y)

# Map function
x = [1, 2, 3]
y = [i + 2 for i in x]
print(y)
c = list(map(lambda i: i + 2, x))
print(c)

# Filter method in list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in x:
    if i % 2 == 0:
        print(i)
print(list(filter(lambda i: i % 2 == 0, x)))

# Printing specific element in multi-dimensional list
List3 = [[1, 2, 3], [5, 6, 7]]
print(len(List3))
print(List3[0][1])

# Unpacking
a, b, c = [1, 2, 3]
print(a)

# Convert multi-dimensional to single dimension
List3 = [[1, 2, 3], [5, 6, 7]]
x = [i for j in List3 for i in j]
print(x)
c = []
for i in List3:
    for j in i:
        c.append(j)
print(c)
