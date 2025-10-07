#Task16
import random

def roll_dice():
    """Rolls a D6 and a D20 and returns their sum."""
    return random.randint(1, 6) + random.randint(1, 20)

def create_player(name):
    """Creates a new player dictionary."""
    return {
        "name": name,
        "wins": 0,
        "scores": []
    }

num_players = int(input("Enter number of players: "))

players = [create_player(input(f"Enter name for Player {i+1}: ")) for i in range(num_players)]

rounds = 0

while max(p["wins"] for p in players) < 3:
    rounds += 1
    print(f"\n🎲 Round {rounds}")

    # Roll for each player
    for p in players:
        score = roll_dice()
        p["scores"].append(score)
        print(f"{p['name']} rolled {score}")

    # Determine round winner
    max_score = max(p["scores"][-1] for p in players)
    winners = [p for p in players if p["scores"][-1] == max_score]

    if len(winners) == 1:
        winners[0]["wins"] += 1
        print(f"🏅 {winners[0]['name']} wins this round!")
    else:
        print("🤝 It's a tie!")

# Determine champion
champion = max(players, key=lambda x: x["wins"])
print(f"\n🏆 {champion['name']} is the champion after {rounds} rounds! 🏆")
