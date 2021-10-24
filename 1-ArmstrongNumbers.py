for i in range(100,2001):
    total = 0
    exponent = len(str(i))
    for j in range(exponent):
        total += int(str(i)[j]) ** exponent
    if total == i:
        print("{} is an armstrong number".format(i))



