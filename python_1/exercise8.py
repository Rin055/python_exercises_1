#ATM simulator

balance = 500
choice = -1
count = 0

while choice != 0:
    print("1) Deposit 2) Withdraw 3) Balance 0) Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        amount = int(input("Amount: "))
        if amount > 0:
            balance += amount
            count += 1
            print("Done.")
        else:
            print("Invalid amount")

    elif choice == 2:
        amount = int(input("Amount: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            count += 1
            print("Take your cash.")

    elif choice == 3:
        print("Balance:", balance)

print("Transactions:", count)
print("Goodbye!")
