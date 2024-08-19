# def append_sum(my_list):
#     for _ in range(3):
#         my_list.append(sum(my_list[-2:]))
#     return my_list
#
# print(append_sum([1, 1, 2]))

# Write a function called process_list that takes a list of numbers,
# doubles each number, removes any that are greater than 10, and then returns the resulting list.

## Failed here ##
# def process_list(i):
#     for i in range(15): i * 2
#     if i > 10: remove(i)
#     return i

## CORRECT ONE, I didn't do this one ##
# def process_list(numbers):
#     result = []
#     for num in numbers:
#         doubled = num * 2
#         if doubled <= 10:
#             result.append(doubled)
#     return result

# def greet_user(name):
#     print(f"Hello {name}!")
# greet_user("aaaa")

# Exercise 1: Basic Function
# Create a function called double_number that takes a number as input and returns twice that number.
# Try implementing this function, then use it to double the number 5 and print the result.

# I think I get it, if you just use return with nothing, it returns "None",
# the function will still work but whatever comes out of the function can('t be used in any other functions,'
# ' whereas when you return the result rather than leaving it empty, it')s like pop()?
# def double_number(number):
#     return number * 2
#
# print(double_number(5))

# Combining Lists
# def combine_sort(mylist1, mylist2):
#   return sorted((mylist1 + mylist2))
#
# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
#


# def double_index(my_list, index):
#     return my_list[:index] + [my_list[index] * 2] + my_list[index + 1:] if 0 <= index < len(my_list) else my_list
#
#
# print(double_index([3, 8, -10, 12], 2))


fruits = ["apple", "banana", "pineapple", "pear", "melon"]
print(f"{fruits[0]} and {fruits[-1]}")
fruits.append("orange")
print(fruits)

middle_fruits = fruits[1:4]
print(middle_fruits)

first_three = fruits[:3]
print(first_three)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1::2]
reversed_odds = numbers[-2::-2]

print("Even numbers:", even_numbers)
print("Reversed odds:", reversed_odds)

numbers2 = [1, 2, 3, 4, 5, 6, 7]
e = len(numbers2) // 2
modified_numbers = numbers2.copy()
modified_numbers[e] = "middle"

print("Middle", modified_numbers)
print("Normal", numbers2)

numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_half = numbers3[:5]
second_half = numbers3[5:]
second_half[-1] = "last"
print(first_half)
print(second_half)

numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_evens = [i ** 2 for i in numbers4 if i % 2 == 0]
doubled_odds = [i * 2 for i in numbers4 if i % 2 != 0]
print("Squared:", squares_of_evens)
print("Doubled odds:", doubled_odds)

numbers5 = [1, 2, 3, 4, 5, 2, 3, 4, 2, 1, 5, 4]