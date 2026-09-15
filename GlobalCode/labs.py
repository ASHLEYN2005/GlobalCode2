
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False

# numbers = [1,56,234,87,4,76,24,69,90,135]
# print([is_even(n) for n in numbers])

# def is_even(number):
#     return number % 2 == 0

# numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
# # even_numbers = [n for n in numbers if is_even(n)]
# # print(even_numbers)


# l = lambda number: number % 2 == 0
# is_even = map(l,numbers)
# print(list(is_even))


# def is_even(number):
#     return number % 2 != 1

# numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
# odd_numbers = [n for n in numbers if not is_even(n)]
# print(odd_numbers)

# def is_even(number):
#     return number % 2 != 1

# numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]

# from functools import reduce
# total = reduce(lambda x, y: x + y, numbers)
# print(total)


# from functools import reduce


# def join_strings(name):
#     names = [ "John", "William"]
#     name = reduce(lambda x, y: x + " " + y, names)
#     print(name)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print([len(word) for word in words])

class Person:
    def __init__(self, name , date_of_birth):
