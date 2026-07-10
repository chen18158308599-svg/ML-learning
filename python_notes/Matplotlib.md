# General Matplotlib Tips

## import

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

## display
`plt.figure()`creates current figure  
`plt.plot()`draws on current axes  
`plt.show()`shows the plot. It does much job for you

## saving figures to file
```python
fig=plt.figure()
fig.savefig('my_figure.png')
```
after this action, the figure will be saved under the same folder as this notebook.  
And in fact, you can save more than just png,
pdf, 
svg, 
jpg, 
jpeg, 
tif, 
eps, 
ps all works.

And later you can display the images you saved by:
```python
from IPython.display import Image
Image('my_figure.png')
```

# two interfaces

## MATLAB-style interface
```python
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(2,1,1) #row,column,panel number
plt.plot(x,np.sin(x))

plt.subplot(2,1,2)
plt.plot(x,np.cos(x))
```
- use `plt.gcf()` and `plt.gca()`to get current figure and get current axes
- note that `plt.subplotsO()`returns figure,axes
- `plt.plot()`returns a list`[<matplotlib.lines.Line2D object>]`

## Object-oriented interface
- this one allows you to go back to the first plot
```python
# First create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)

# Call plot() method on the appropriate object
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
```
- here `.plot()`is a method for axes objects, so, define ax before doing `ax.plot()`

# simple line plots

## creating figures and axes
```python
fig = plt.figure()
ax=plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
```

## Adjusting the Plot: Line Colors and Styles
### color
- specific name: `'blue'`,`'red'`...
- short: `'r'`,`'g'`...(rgbcmyk)
- grayscale: `'0.75'`...
- hex code
- RGB
- HTML

Example:
```python
plt.plot(x,np.sin(x),color='r')
```
### linestyle
- `solid` `'-'`
- `dashed` `'--'`
- `dashdot` `'-.'`
- `dotted` `':'`

Example:
```python
plt.plot(x,np.sin(x),linestyle='-')
```

### combination
Example:
`plt.plot(x, x + 0, '-g') # solid green`

## Adjusting the Plot: Axes Limits

Setting limits for x-axis and y-axis:
```python
plt.xlim(0,10)
plt.ylim(-1,1)
```
A more convenient way:
```python
plt.axis([0,10,-1,1])
# set limits in one line
plt.axis('tight')
#make the graph arrangement tighter(no blank at edges)
plt.axis('equal')
#makes one unit on the x-axis equal in length to one unit on the y-axis.
```

Example:

```python
import matplotlib.pyplot as plt
import numpy as np

x=
plt.figure()
plt.plot(x,np.sin(x))
```

### Labeling Plots

```python
plt.title('this is the title')
plt.xlabel('this is the x-label')
plt.ylabel('same')
plt.legend() 
```
In object-oriented interface, things get different:
- plt.xlabel() → ax.set_xlabel()
- plt.ylabel() → ax.set_ylabel()
- plt.xlim() → ax.set_xlim()
- plt.ylim() → ax.set_ylim()
- plt.title() → ax.set_title()

## Simple Scatter Plots