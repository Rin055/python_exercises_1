#Euclid's algorithm

a = int(input("a = "))
b = int(input("b = "))

x = a
y = b

while b != 0:
    print("(", a, ",", b, ")")
    a, b = b, a % b

print("GCD =", a)
print("LCM =", x * y // a)
