```
Write a function log_scale(data, base) that takes a list of positive numbers data, 
and a logarithmic base, and returns a new list with the logarithm of each number in the original list, 
using the given base.
```
import math


def log_scale(data, base):
    scaled_data = []
    for i in data:
        scaled_data.append(math.log(i, base))
    return scaled_data
