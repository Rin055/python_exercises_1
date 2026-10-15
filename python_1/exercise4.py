#Rice on a chessboard

grains = 1
total = 0

for square in range(64):
    total += grains
    grains *= 2

print("Total grains:", total)
print("Tonnes:", total * 0.02 / 1000000)
