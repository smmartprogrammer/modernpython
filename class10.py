# from typing import Callable

# add: Callable[[int, int], int] = lambda x, y: x + y
# result = add(10,20) # result will be 30
# print(result)

# from typing import Tuple, Dict, Any
# def my_function(a:int , b:int , *abc:Tuple, **xyz:dict[str,int]) -> None:
#     print(a, b, abc, xyz)

# my_function(1, 2, 3, 9, 9,  c=20, d=30, x=100)
          
from typing import Callable

def decorator(func: Callable[[int], None]) -> Callable[[int], None]:
    def wrapper(num1:int) -> None:
        print("raghunathji before function called")
        func(num1)
        print("raghunathji after function called")
    return wrapper

@decorator
def say_hello(num1:int)->None:
    print(num1)

say_hello(100)