list = input("Enter your list elements with " ": ").split()
i = 2
while len(list) >= 0:
    if len(list)>=2:
        list.pop(i)
        print(list)
        if i >= len(list):
            i = 2
        else:
            i += 2
    else:
        list.pop()
        print(list)