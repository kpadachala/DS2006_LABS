import random

rounds = 5
player1_rolls = []
player2_rolls = []

for i in range(rounds):
    player1_rolls.append(random.randint(1, 6))
    player2_rolls.append(random.randint(1, 6))

print(player1_rolls)
print(player2_rolls)

print("-----------------------------------------")
print("| Round    | " + " | ".join(str(i+1) for i in range(rounds)) + " |")
print("-----------------------------------------")
print("| Player 1 | " + " | ".join(str(r) for r in player1_rolls) + " |")
print("-----------------------------------------")
print("| Player 2 | " + " | ".join(str(r) for r in player2_rolls) + " |")
print("-----------------------------------------")

filename = input("Enter a filename to save the summary: ")
with open(filename, "w") as f:
    f.write("-----------------------------------------\n")
    f.write("| Round    | " + " | ".join(str(i+1) for i in range(rounds)) + " |\n")
    f.write("-----------------------------------------\n")
    f.write("| Player 1 | " + " | ".join(str(r) for r in player1_rolls) + " |\n")
    f.write("-----------------------------------------\n")
    f.write("| Player 2 | " + " | ".join(str(r) for r in player2_rolls) + " |\n")
    f.write("-----------------------------------------\n")

