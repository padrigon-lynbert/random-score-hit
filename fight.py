import random
import time

choices = [1000, 1500, 3000]
weights = [3, 2, 1]

enemy = random.randint(15000, 50000)

while enemy>=0:
    hit = random.choices(choices, weights=weights)[0]
    enemy = enemy - hit
    print(f"enemy HP: {enemy}"); time.sleep(.3)