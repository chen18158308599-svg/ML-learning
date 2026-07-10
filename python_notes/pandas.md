# data selection
## Series
### series as dictionary
- We can use dictionary-like python expressions and methods:
```python
data.keys()
list(data.items())
```
- You can even extend a Series by assigning to a new index value
```python
data['new index']=1.7
```
### series as one dimensional array
- `data['a':'c']` slice from index a to c (**include** c)
- `data[0:2]` slice from index 0 to 1 (**excluded** 2)
- masking: `data[(data > 0.3) & (data < 0.8)]`  
  - **note:** the key is that you can do `data[True, False...]`to a series.
- fancy indexing: `data[['a','c']]`only returns item a and c
  - **note:** for one item, we just use `data['a']`

**important**  
- if your Series has an explicit integer index, an indexing operation such as `data[1]` will use the **explicit indices**, while a slicing operation like `data[1:3]` will use the **implicit** Python-style index.
### indexers: attributes to avoid confusion
- loc: always refers to the **explicit index**
```python
data.loc[1]
data.loc[1:3]
```
- iloc: always refers to the **inplicit index**
- ix
## DataFrame
### DataFrame as a dictionary
- you can call a single column
```python
df['column0'] #dictionary style
df.column0 #attribute style
#These two gives the exact same result
```
**important**  
for some DataFrame methods, such as `df.pop()`, `df.pop` gives a different result.
```python
df.pop is df.['pop']
#the expression returns False
```
- like Series, you can modify the DataFrame objects
```python
df['density'] = df['pop'] / df['area']
df.iloc[0,2]=90
```
### DataFrame as two-dimensional array
- some attributes:
```python
data.values #examine the values
data.T #transpose
```
- `data.values[0]` returns a row
- `data['column0']` returns a column
### indexers
```python
data.iloc[:3,:2] #row 0~2, column 0~1
data.loc[:'row2',:'column1']
data.ix[:3,:'column1'] #hybrid
```
- you can even integrate fancy index with masking:  
```python
data.loc[data.density > 100, ['pop', 'density']]
```
### additional indexing conventions
while indexing refers to columns, slicing refers to rows
```python
data['row1':'row3']
data[1:4]
#returns row1 to row3
data[data.column2 > 100]
#returns rows
```
# Operation on Data in Pandas
## Ufuncs: Index Preservation
**any NumPy ufunc will work on Pandas Series and DataFrame objects**
For example:
```python
import pandas as pd
import numpy as np
rng=np.random.RandomState(4)
data=pd.DataFrame(rng.randint(0,10,(3,4)),index=['a','b','c'],columns=['A', 'B', 'C', 'D'])
np.exp(data) #NumPy ufun works
```
## UFuncs: Index Alignment
### align in series
- when we apply ufuncs to two series, the values automatically match by index.
- **note**: to fill unmatched items, use `fill_value=0`
```python
A.add(B, fill_value=0)
```
### align in dataframe
- basically the same as series

| operator | pandas methods             |  
|----------|----------------------------|  
| +        | add()                      |
| -        | sub(), subtract()          |
| *        | mul(), multiply()          |
| /        | truediv(), div(), divide() |
| //       | floordiv()                 |
| %        | mod()                      |
| **       | pow()                      |
## Ufuncs: Operations Between DataFrame and Series
Operations between a **DataFrame** and
a **Series** are similar to operations between a two-dimensional and one-dimensional NumPy array.
```python
#Row-wise
df = pd.DataFrame(A, columns=list('QRST'))
df - df.iloc[0]
#Column-wise
df.subtract(df['R'], axis=0) #axis=0 means 把series竖起来减
```
- **note**: these DataFrame/Series operations will automatically align indices between the two elements  
**Pandas matches labels before doing math**
# Handling missing data
- **sentinel value**: A sentinel value is a special value used to **signal a particular condition**, rather than representing normal data.  
- a sentinel value can be some data-specific convention like **-999**, or a global convention like **NaN**.
## None: Pythonic missing data
-  None is considered an **object** in numpy array, and it slows down the calculation.
- with None, you get an error with aggregations like `sum()`.
## NaN: Missing numerical data
- floating-point value instead of object
- support fast operations given to its type
- aggregates are well-defined
- 