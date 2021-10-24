"""
Input : n = 2
         List_1 = [1, 2, 3, 4, 5, 6]
Output : List_1 = [5, 6, 1, 2, 3, 4]
We get output list after right rotating
(clockwise) given list by 2.

Input :  n = 3
         List_1 = [3, 0, 1, 4, 2, 3]
Output : List_1 = [4, 2, 3, 3, 0, 1]
"""
n=int(input("write a number : "))
liste = [1, 2, 3, 4, 5, 6, 7]
while n >=0:
    liste.append(liste.pop(0))
    n-= 1
print(liste)

