square = 1

while square <= 10:
    print(square)    # This code is executed 10 times
    square += 1      # This code is executed 10 times

print("Finished")  # This code is executed once

square = 0
number = 1

while square <= 99 and number < 10:
    square = number ** 2
    print(square)
    number += 1

# Solution from teacher
#
# while square < 81:
#     square = number ** 2
#     print(square)
#     number += 1