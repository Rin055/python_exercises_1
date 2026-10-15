#Savings goal

goal = int(input("Goal: "))

saved = 0
weekly = 50
weeks = 0

while saved < goal:
    saved += weekly
    weeks += 1
    last_week = weekly
    weekly += 5

print(f"Goal reached in {weeks} weeks. Saved: {saved} GEL")
print(f"Saved in the last week: {last_week} GEL")

