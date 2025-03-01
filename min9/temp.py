import random

chars = [chr(i) for i in range(48, 125)]

with open("data.txt", "w") as f:
    for _ in range(1000000):
        random.shuffle(chars)
        f.write(f"{''.join(chars[:20])}\n")