# # example 1

# from typing import Union

# grade : Union[int, float] = 7.0

# print(grade)

# # example 1
# from typing import Union

# per : Union[int, float] = int(input("Please enter your percentage:\t "))
# grade : Union[str, None] = None

# if per >= 80:
#     grade = "A+"
# elif per >= 70:
#     grade = "A"
# elif per >= 60:
#     grade = "B"
# elif per >= 50:
#     grade = "C"
# elif per >= 40:
#     grade = "D"
# elif per >= 33:
#     grade = "E"
# else :
#     grade = "F"

# print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade} " )

# from typing import Union, Optional

# per : Union[int, float] = int(input("Please enter your percentage:\t "))
# grade : Optional[str] = None

# if (per >= 0) and (per < 33):
#     grade = "Fail"
# elif (per >= 33) and (per < 40):
#     grade = "E"
# elif (per >= 40) and (per < 50):
#     grade = "D"
# elif (per >= 50) and (per < 60):
#     grade = "C"
# elif (per >= 60) and (per < 70):
#     grade = "B"
# elif (per >= 70) and (per < 80):
#     grade = "A"
# elif (per >= 80) and (per <= 100) :
#     grade = "A+"

# print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade} " )

from typing import Union
perType = Union[float, int]

percentages : list[perType] = [80, 99.9, 50,51, 65,70]
grades : list[str] = []

for per in percentages:
    grade : str = ""

if (per >= 0) and (per < 33):
    grade = "Fail"
elif (per >= 33) and (per < 40):
    grade = "E"
elif (per >= 40) and (per < 50):
    grade = "D"
elif (per >= 50) and (per < 60):
    grade = "C"
elif (per >= 60) and (per < 70):
    grade = "B"
elif (per >= 70) and (per < 80):
    grade = "A"
elif (per >= 80) and (per <= 100) :
    grade = "A+"

    grades.append(grade)


print(percentages)
print(grades)