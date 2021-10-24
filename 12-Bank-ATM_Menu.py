
print("""
Welcome Python-Addicts ATM 
Transactions
1. Withdrawal
2. Deposit
3. Balance Inquiry
4. Exit
""")
balance = 0
while True:
    transaction = input("Transaction: ")

    if transaction == "4":
        print("Program is ending\nGood-bye")
        break
    elif transaction == "1":
        withdrawn = int(input("Amount to be withdrawn: "))
        if withdrawn > balance:
            print("Your balance is {} $".format(balance))
            print("insufficient balance\ntry again with lower amount")
        else:
            balance -= withdrawn
    elif transaction == "2":
        deposit = int(input("Amount to be deposited: "))
        balance += deposit
        print("your transaction is complete")
    elif transaction == "3":
        print("Your balance is {} $".format(balance))

