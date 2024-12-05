#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def sample_dist(x, mu, sigma, n, n_sample):

    samples = []
    for i in range(n_sample):
        samples.append(np.random.normal(loc=mu, scale=sigma, size=n))

    means = []
    for i in samples:
        means.append(np.mean(i))

    average = np.mean(means)
    stdev = np.std(means)
    z = (x - mu)/(sigma/np.sqrt(n))
    p_val = norm.sf(abs(z))

    plt.hist(means, edgecolor='k', bins=20)
    plt.show()

    return average, stdev, z, p_val

av, sd, z, p = sample_dist(110, 100, 15, 10, 1000)
print(f"The mean of sampling distribution = {av:.4f}")
print(f"The standard deviation of sampling distribution = {sd:.4f}")
print(f"The z-score = {z:.4f}")
print(f"Probability = {p:.4f}")
"""
samples = []
for i in range(1000):
    samples.append(np.random.normal(loc=100, scale=15, size=9))

means = []
for i in samples:
    means.append(np.mean(i))

plt.hist(means, edgecolor='k', bins=20)
plt.show()


samples = []
for i in range(1000):
    samples.append(np.random.normal(loc=100, scale=15, size=25))

means = []
for i in samples:
    means.append(np.mean(i))

plt.hist(means, edgecolor='k', bins=20)
plt.show()


samples = []
for i in range(1000):
    samples.append(np.random.normal(loc=100, scale=15, size=10))

means = []
for i in samples:
    means.append(np.mean(i))

plt.hist(means, edgecolor='k', bins=20)
plt.show()

average = np.mean(means)
stdev = np.std(means)
z = (110-100)/(15/np.sqrt(10))
p_val = norm.sf(abs(z))
print(f"Mean = {average:.2f}")
print(f"Standard Deviation = {stdev:.2f}")
print(f"z-Score = {z:.2f}")
print(f"p-value = {p_val:.2f}")
print(f"Probability = {p_val*100:.2f}%")
"""
