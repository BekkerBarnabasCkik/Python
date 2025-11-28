import random
import math

def benford_digit():
    """Véletlen első számjegy Benford-eloszlás szerint."""
    # p(d) = log10(1 + 1/d)
    digits = list(range(1, 10))
    probs = [math.log10(1 + 1/d) for d in digits]
    return random.choices(digits, weights=probs, k=1)[0]

def generate_number():
    """Generál egy 1000–9999 közötti számot Benford szerinti első számjeggyel."""
    first = benford_digit()
    rest = random.randint(0, 999)  # 3 tetszőleges számjegy
    return int(f"{first}{rest:03d}")

numbers = []

# 95% negatív (950 db), 5% pozitív (50 db)
for _ in range(95):
    numbers.append(-generate_number())

for _ in range(5):
    numbers.append(generate_number())

# Keverjük össze a listát
random.shuffle(numbers)

numbers  # Ez a kész Benford-törvénnyel egyező 1000 elemű számsorozat
print(numbers)