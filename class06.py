# example 1

from typing import Union

grade : Union[int, float] = 7.0

print(grade)

# example 1
from typing import Union

per : Union[int, float] = int(input("Please enter your percentage:\t "))
grade : Union[str, None] = None

if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else :
    grade = "F"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade} " )