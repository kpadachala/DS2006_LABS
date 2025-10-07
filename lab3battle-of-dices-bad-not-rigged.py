import random

# Round 1
player1_round1_roll = random.randint(1, 6)
player2_round1_roll = random.randint(1, 6)

# Round 2
player1_round2_roll = random.randint(1, 6)
player2_round2_roll = random.randint(1, 6)

# Round 3
player1_round3_roll = random.randint(1, 6)
player2_round3_roll = random.randint(1, 6)

# Print results
print("Round 1: Player 1 =", player1_round1_roll, "| Player 2 =", player2_round1_roll)
print("Round 2: Player 1 =", player1_round2_roll, "| Player 2 =", player2_round2_roll)
print("Round 3: Player 1 =", player1_round3_roll, "| Player 2 =", player2_round3_roll)

print("-----------------------------------------")
print("| Round    | 1 | 2 | 3 |")
print("-----------------------------------------")
print(f"| Player 1 | {player1_round1_roll} | {player1_round2_roll} | {player1_round3_roll} |")
print("-----------------------------------------")
print(f"| Player 2 | {player2_round1_roll} | {player2_round2_roll} | {player2_round3_roll} |")
print("-----------------------------------------")

