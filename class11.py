a: list[str] =['a', 'b'] # mutable
b: list[str] =['c', 'd'] # mutable

print(id(a))
print(id(b))

print(2+5)
print(a+b)
print(a-b) # it should be plus sign, but mistakenly some developer has put minus, so it is not performing the 
            # correct answer, so this sort of issues will going to be check through test handling, 