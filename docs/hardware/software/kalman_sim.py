import numpy as np
import matplotlib.pyplot as plt

# Simple Allan-deviation simulator for our magic-angle gyro
f0 = 24100  # Hz
Q = 1e5     # conservative starting value
tau = np.logspace(-1, 3, 100)  # averaging time 0.1s to 1000s

sigma = (1 / (2 * np.pi * f0 * Q)) * np.sqrt(1e-3 / tau)  # rough kT/P term

plt.loglog(tau, sigma * 180/np.pi * 3600)  # °/h
plt.xlabel('Averaging time τ (s)')
plt.ylabel('Bias instability (°/h)')
plt.title('Predicted Allan Deviation — MA-INS-Open')
plt.grid(True)
plt.show()

print("Target bias stability at τ=60 s:", sigma[50]*180/np.pi*3600, "°/h")
