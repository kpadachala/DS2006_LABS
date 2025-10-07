# dice.py
import random

def rollD4():
    """
    Roll a 4-sided dice (D4).
    Returns: int (1–4)
    """
    return random.randint(1, 4)

def rollD6():
    """
    Roll a 6-sided dice (D6).
    Returns: int (1–6)
    """
    return random.randint(1, 6)

def rollD8():
    """
    Roll an 8-sided dice (D8).
    Returns: int (1–8)
    """
    return random.randint(1, 8)

def rollD12():
    """
    Roll a 12-sided dice (D12).
    Returns: int (1–12)
    """
    return random.randint(1, 12)

def rollD20():
    """
    Roll a 20-sided dice (D20).
    Returns: int (1–20)
    """
    return random.randint(1, 20)

def rollD100():
    """
    Roll a 100-sided dice (D100).
    Returns: int (1–100)
    """
    return random.randint(1, 100)

# Quick test (only runs if you execute dice.py directly)
if __name__ == "__main__":
    print("D4:", rollD4())
    print("D6:", rollD6())
    print("D8:", rollD8())
    print("D12:", rollD12())
    print("D20:", rollD20())
    print("D100:", rollD100())
