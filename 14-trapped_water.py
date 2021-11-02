liste = [3,1,2,0,5,0,2]

left_max = 0
right_max = 0
result = 0
lo = 0
hi = len(liste)-1
while (lo <= hi):
    if liste[lo] < liste[hi]:
        if liste[lo] > left_max:
            left_max = liste[lo]
        else:
            result += left_max - liste[lo]
        lo += 1
    else:
        if liste[hi] > right_max:
            right_max = liste[hi]
        else:
            result += right_max - liste[hi]
        hi -= 1
print(result)