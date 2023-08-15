import random
red = 0; blue = 0

while True:
    hit = random.choice([3, 4, 5])
    
    score_to = random.choice(['Red', 'Blue'])

    if score_to == "Red":
        red += hit
        print(f"{score_to}: {red}")
        if red >= 50:
            print(f"\n{score_to}: {red}")
            print(f"{score_to}: {blue}")
            break
    else:
        blue += hit
        print(f"{score_to}: {blue}")
        if blue >= 50:
            print(f"\n{score_to}: {red}")
            print(f"{score_to}: {blue}")
            break
