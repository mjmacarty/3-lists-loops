"""
Lists & Loops
| - lists allow programmers to store any number & any
|  combination of Python objects in one variable
| - loops allow programmers to execute the same block open
|  repeatedly
"""

#choices = ["rock", "paper", "scissors"]
#print(len(choices))

#for item in choices:
#    print(item)

#for i in range(10):
#    print(i) 

numbers = list(range(1,11))
squares = []

for number in numbers:
    squares.append(number ** 2)
#print(squares)   

print("{:10s}{:>10s}".format("Number", "Square"))
print("-"*20)
#print("1"+"1")
for index in range(len(numbers)):
    print("{:<10d}{:10d}".format(numbers[index], squares[index]))
