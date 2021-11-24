#%%
from typing import Generator, Iterator
import copy

def deep_flatten(inputs: list) -> list:
    """
    [1, [3, [2]]]
    -> 1
    -> [3, [2]]
        -> 3, [2]
          -> 3
            -> 2
    """
    output = []
    for el in inputs:
        if isinstance(el, (int,str)):
            output.append(el)
        else:
            output.extend(deep_flatten(list(el)))
    yield from output
    
# %%
