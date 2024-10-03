#!/usr/bin/env python3


from random import randint
import matplotlib.pyplot as plt


flip_count = 1
heads = []
head_prob = []
flips = []

while flip_count <= 100:
    flip = randint(0, 1)
    flips.append(1)
    if flip == 1:
        heads.append(1)
    head_prob.append(len(heads)/len(flips))
    flip_count += 1

plt.figure(figsize=(8, 7))
plt.scatter(range(1, 101), head_prob)
plt.plot([-1, 101], [0.5, 0.5], '-k')
plt.xlim([-1, 101])
plt.ylim([-0.1, 1.1])
plt.xlabel("Number of Flips", size=12, weight='bold')
plt.ylabel("Probability of Heads", size=12, weight='bold')
plt.xticks(size=12, weight='bold')
plt.yticks(size=12, weight='bold')
plt.show()
