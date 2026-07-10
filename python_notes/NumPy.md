### how to use `RandomState`
```python
import numpy as np
rng=np.random.RandomState(42)
x=rng.randint(0,10,4) 
#using rng. means you want to fix this randint
```

### don't know what it is
- both`np.zeros(4)`and`np.zeros((4,))`give the same outputs. 
  - the first one is a convenient way
  - the second one is a tuple

### little tricks
instead of:
```python
m=X.shape[0]
n=X.shape[1]
```
use:
```python
m,n=X.shape
```
surprised to see how tuple performs like this