#Input validation

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

month = int(input("Month (1-12): "))

while month < 1 or month > 12:
    print("Invalid, Try again.")
    month = int(input("Month (1-12): "))

print("You chose month", month)
print(months[month - 1])