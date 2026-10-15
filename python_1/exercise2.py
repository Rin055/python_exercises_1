#Stop at zero

number = int(input("Number: "))
count = 0
total = 0

while number != 0:
    count += 1
    total += number

    if count == 1 or number > largest:
        largest = number

    number = int(input("Number: "))

print("Count:", count)
print("Sum:", total)

if count > 0:
    print("Average:", round(total / count, 2))
    print("Largest:", largest)
else:
    print("Average: 0")
    print("Largest: None")
