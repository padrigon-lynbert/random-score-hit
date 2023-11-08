import matplotlib.pyplot as plt
from MeanMedianMode.math_algorithms.mean import mean
import random
import time
red, blue = list(), list()
RED, BLUE = [], []

while True:
    hit = random.choice([3, 4, 5])
    score_to = random.choice(['Red', 'Blue'])

    if score_to == "Red":
        try:
            red.append(hit)
            RED.append(sum(red)+hit)
            BLUE.append(BLUE[-1])
        except IndexError:
            BLUE.append(0)

        print(f"{score_to}: {sum(red)}")
        time.sleep(.5)

        if sum(red) >= 50:
            break

    else:

        try:
            blue.append(hit)
            BLUE.append(sum(blue)+hit)
            RED.append(RED[-1])
        except IndexError:
            RED.append(0)

        print(f"{score_to}: {sum(blue)}")
        time.sleep(.5)

        if sum(blue) >= 50:
            break

if (sum(red) > sum(blue)): print(f"\nred: {sum(red)} (winner)")
else: print(f"\nblue: {sum(blue)} (winner)")


print("MATCH INFO")
print(f"Average score points: |Red: {round(mean(red),1)} vs {round(mean(blue),1)} : Blue|")


plt.plot(RED, label="red", color="red")
plt.plot(BLUE, label="blue", color="blue")
plt.xlabel('Time')
plt.ylabel('Score')

plt.title(f"Teams\nMatch Info: ")

plt.legend()
plt.text(0, RED[0], sum(red), fontsize=12, color='red', ha='left', va='bottom')
plt.text(0, BLUE[0], sum(blue), fontsize=12,
         color='blue', ha='left', va='bottom')

plt.show()
