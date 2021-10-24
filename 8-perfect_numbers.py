number = int(input("Number: "))
total = sum([i for i in range(1, number) if number % i == 0])
if total == number:
    print("{} is a perfect number".format(number))
