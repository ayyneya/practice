""" - - - Exercise: Favorite Fruits
import time

countdown = 10

while countdown > 0:
  print("Number: " + str(countdown))
  countdown -= 1
  time.sleep(1)

print("We have liftoff!")
"""


""" - - - Exercise: Favorite Fruits
Create a list called favorite_fruits that contains the names of your favorite fruits.
Use a loop to print a message for each fruit in the list, saying "I love eating [fruit name]!"
After the loop, print a final message saying "Fruits are a healthy and delicious snack!"

import time

favorite_fruits = ["apple", "banana", "orange", "strawberry", "kiwi"]

length = len(favorite_fruits)
index = 0

while index < length:
    print("I love eating " + favorite_fruits[index])
    index += 1
    time.sleep(2)
"""

""" - - - Exercise: Counting Numbers
Create a list called numbers that contains the following values: 1, 2, 3, 4, 5.
Use a loop to iterate over the list and print each number.
Multiply each number by 2 and print the result.
After the loop, print a message saying "Multiplication complete!"

numbers = [1, 2, 3, 4, 5]

amount = len(numbers)
index = 0

while index < amount:
    print(numbers[index]*2)
    index += 1
"""

""" - - - Understanding
import time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(letters)):
    print(letters[i])
    time.sleep(0.5)

### Length of letters variable = 8, the range of the length is 0-7.
### i is a temporary variable that takes on the value of an element in the list on each iteration of the loop
### on the first iteration, a = i, on the second, b = i, etc.
### print(letters[i]) prints a list element with the i variable on each iteration
"""
