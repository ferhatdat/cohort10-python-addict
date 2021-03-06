"""
A jumbled list is given whose elements are consecutive numbers. Write python code that outputs even numbers of missing numbers that are between the smallest element and the largest element of the list, but not shown in the list.
Input
liste = [48, 10, 11, 21, 36, 5, 6, 52, 28, 29, 53, 54, 45, 19, 20, 47, 55, 39, 41, 7, 9, 17, 26, 27, 42, 22, 37, 51, 46, 18, 44, 30, 34, 13, 15, 35, 33, 16, 50, 24]
Expected Output:
8 12 14 32 38 40 (edited)
"""
liste = [48, 10, 11, 21, 36, 5, 6, 52, 28, 29, 53, 54, 45, 19, 20, 47, 55, 39, 41, 7, 9, 17, 26, 27, 42, 22, 37, 51, 46, 18, 44, 30, 34, 13, 15, 35, 33, 16, 50, 24]

print(*(i for i in set(range(min(liste), max(liste)+1)) - set(liste) if i % 2 ==0))

