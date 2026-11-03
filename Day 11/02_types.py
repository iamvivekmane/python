# type definitions are used to explicitly specify the type of a variable
a : int = 10
def add(a:int,b:int)->int:
    return a + b


# this annotations helps in making the code self documented  
from typing import List, Union , Dict, Tuple

# list of integers
numbers: List[int] = [1,2,3,4,5]

# tuple of strings
names: Tuple[str] = ['this','is','random','string']