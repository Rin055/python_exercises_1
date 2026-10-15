#Reverse a number

n = int(input("Number: "))
original = n
rev = 0
count = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
    count += 1

print("Reversed:", rev)
print("Digits:", count)

if original == rev:
    print("It is a palindrome!")
else:
    print("It is not a palindrome!")
