string = "Hello World"
# string[0] = "h"

# Traceback (most recent call last):
#   File "E:\Python\02_Tuples.py", line 2, in <module>
#     string[0] = "h"
#     ~~~~~~^^^
# TypeError: 'str' object does not support item assignment

# So string are immutable by default, now there are workarounds that can be
# done to mutate a string

# 1. Replace method

string = string.replace("H", "h", 1)
print(string)

# Tuples : Immutable lists

newTuple = ("Hello", "World", "Python", "JavaScript")

for index, word in enumerate(newTuple):
    print(f"{index+1}. {word}")
