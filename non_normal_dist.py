#!/usr/bin/env python3

import random
import statistics as stats
import matplotlib.pyplot as plt

sample_size = int(input("Enter the sample size: "))

population = []
for i in range(147*sample_size):
    population.append(1)
for i in range(361*sample_size):
    population.append(2)
for i in range(187*sample_size):
    population.append(3)
for i in range(168*sample_size):
    population.append(4)
for i in range(83*sample_size):
    population.append(5)
for i in range(34*sample_size):
    population.append(6)
for i in range(12*sample_size):
    population.append(7)
for i in range(4*sample_size):
    population.append(8)
for i in range(2*sample_size):
    population.append(9)
for i in range(2*sample_size):
    population.append(10)

random.shuffle(population)
print(stats.mean(population))
print(stats.stdev(population))
print(len(population))
samples = []
counter = 0
for i in range(1000):
    sample = []
    for j in range(sample_size):
        sample.append(population[counter])
        counter += 1
    samples.append(sample)

counter = 1
for i in samples:
    print(counter, i)
    counter += 1

means = []
for i in samples:
    means.append(stats.mean(i))

counter = 1
for i in range(len(samples)):
    print(counter, samples[i], means[i])
    counter += 1

plt.hist(means, bins=20, edgecolor='k')
plt.show()

