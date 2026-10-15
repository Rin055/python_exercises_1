#Digital root

n = int(input("Number: "))
original = n

while n >= 10:
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    n = total
    print("->", n)

print("Digital root:", n)

if original == 0:
    formula = 0
else:
    formula = 1 + (original - 1) % 9

print("Formula:", formula)
