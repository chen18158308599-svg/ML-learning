# attribute & method
## origin of my confusion
parentheses with these functions:
```python
df.index
df.items
df.values
df.keys
```
## concepts
**object:**   
In python, things like ```'hello'``` ```[1,2,3]``` are all objects.  
objects contain two things: **data and behavior** 

**attribute:**  
An attribute is simply **information** stored inside an object. Think of it as a property of the object.  
Attribute doesn't need parentheses

**method:**  
A method is **a function attached** to an object. It defines what the object can do.  
Method need parentheses.

## role of parentheses
so basically, without (), ```df.index```means the function itself. But with (), it will give the result.

## conclusion

```python
#These are all attributes:
df.index
df.columns
df.values
```

```python
#These are methods:
df.items()
df.keys()
```

# iterator

## what is iterator?

An iterator is an object that produces values **one at a time** when requested.

Instead of storing all results at once, it generates them step by step.

## How to recognize an iterator
common iterators include:
```python
range()
zip()
map()
filter()
df.items()
```

## How to see the values
- use ```list(iterator)```

# copy and deepcopy
## copy only works for simple lists
```python
b = a.copy()
```
or:
```python
import copy
b = copy.copy(a)
```

when encountering:
- lists inside lists
- dictionaries inside lists
- NumPy arrays inside objects
- complex data structures (very common in ML)
  
it doesn't work

## deepcopy
```python
import copy
b = copy.deepcopy(a)
```

Example:
```python
a = [[1,2], [3,4]]
b = copy.deepcopy(a)

b[0][0] = 100
```