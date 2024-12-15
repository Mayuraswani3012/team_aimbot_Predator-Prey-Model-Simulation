# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14zHjHXnCZoAQYK4aWnaXfkgXQF3zcNx8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the predator-prey model (Lotka-Volterra equations)
def predator_prey(y, t, alpha, beta, delta, gamma):
    prey, predator = y
    dydt = [alpha * prey - beta * prey * predator,  # Prey population change
            delta * prey * predator - gamma * predator]  # Predator population change
    return dydt

# Parameters
alpha = 0.1  # Prey birth rate
beta = 0.02  # Predation rate
delta = 0.01  # Predator reproduction rate
gamma = 0.1  # Predator death rate

# Initial populations
prey_init = 40
predator_init = 9
y0 = [prey_init, predator_init]

# Time points
t = np.linspace(0, 200, 1000)

# Solve the differential equations
solution = odeint(predator_prey, y0, t, args=(alpha, beta, delta, gamma))
prey, predator = solution.T

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, prey, label="Prey Population", color="blue")
plt.plot(t, predator, label="Predator Population", color="red")
plt.title("Predator-Prey Dynamics")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid()
plt.show()

# Phase Plot: Predator vs. Prey Population
plt.figure(figsize=(10, 6))
plt.plot(prey, predator, color="purple")
plt.title("Phase Plot: Predator vs. Prey")
plt.xlabel("Prey Population")
plt.ylabel("Predator Population")
plt.grid()
plt.show()

# Histogram: Prey Population Distribution
plt.figure(figsize=(10, 6))
plt.hist(prey, bins=30, color="blue", alpha=0.7)
plt.title("Prey Population Distribution")
plt.xlabel("Prey Population")
plt.ylabel("Frequency")
plt.grid()
plt.show()

# Histogram: Predator Population Distribution
plt.figure(figsize=(10, 6))
plt.hist(predator, bins=30, color="red", alpha=0.7)
plt.title("Predator Population Distribution")
plt.xlabel("Predator Population")
plt.ylabel("Frequency")
plt.grid()
plt.show()

# Combined Plot: Prey and Predator Population Over Time
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Time')
ax1.set_ylabel('Prey Population', color=color)
ax1.plot(t, prey, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Predator Population', color=color)
ax2.plot(t, predator, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title("Prey and Predator Population Over Time")
plt.grid()
plt.show()