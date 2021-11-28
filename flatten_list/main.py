#%%
def deep_flatten(inputs: list) -> list:
    """
    [1, [3, [2]]]
    -> 1
    -> [3, [2]]
        -> 3, [2]
          -> 3
            -> 2
    """
    for el in inputs:
        if isinstance(el, (int,str)):
            yield el
        else:
            yield from deep_flatten(el)
    