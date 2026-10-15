#Collatz sequence

n = int(input("n = "))
steps = 0

while n != 1:
    print(n, end=" ")

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    steps += 1

print(1)
print("Steps:", steps)