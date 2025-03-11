import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
distances_cm = np.array([0.2, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0])  
# Three repeated voltage measurements at each distance:
voltage_v2 = np.array([20,   47,  56.3, 50, 46, 43, 36])
voltage_v3 = np.array([21,   51,  58,   53, 48, 35.9, 34])
voltage_v4 = np.array([21,   45,  55,   50, 47, 43,   32])
# 2. Mean & Standard Deviation
V_mean = np.mean([voltage_v2, voltage_v3, voltage_v4], axis=0)
V_std  = np.std([voltage_v2, voltage_v3, voltage_v4], axis=0, ddof=1)
# 3. Plot: Voltage vs. Distance
plt.figure(figsize=(6,4))
plt.errorbar(distances_cm, V_mean, yerr=V_std, color='blue',
             ecolor='red', label='Data (mean ± std)')
plt.title('Voltage vs. Plate Distance')
plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.show()
# 4. Plot: 1/Voltage vs. 1/Distance
inv_V = 1.0 / V_mean
inv_x = 1.0 / distances_cm
# For error bars in 1/V, propagate the uncertainty:
inv_V_std = V_std / (V_mean**2)
plt.figure(figsize=(6,4))
plt.errorbar(inv_x, inv_V, yerr=inv_V_std, capsize=5, color='blue', label='Data (1/V vs. 1/x)')
plt.title('1/Voltage vs. 1/Distance')
plt.xlabel('1 / Distance (1/cm)')
plt.ylabel('1 / Voltage (1/V)')
plt.grid(True)
plt.legend()
plt.show()
# 5. Linear Regression on 1/V vs. 1/x
slope, intercept, r_value, p_value, std_err = stats.linregress(inv_x, inv_V)
print("=== Linear Regression: 1/V vs. 1/x ===")
print(f"Slope     = {slope:.4f} (1/V per (1/cm))")
print(f"Intercept = {intercept:.4f} (1/V)")
print(f"R-squared = {r_value**2:.4f}")
print("--------------------------------------")
# Plot the best-fit line
fit_line = slope * inv_x + intercept
plt.figure(figsize=(6,4))
plt.errorbar(inv_x, inv_V, yerr=inv_V_std, color='blue',
             ecolor='red', label='Data')
plt.plot(inv_x, fit_line, 'r--', label='Linear Fit')
plt.title('1/Voltage vs. 1/Distance (Linear Fit)')
plt.xlabel('1 / Distance (1/cm)')
plt.ylabel('1 / Voltage (1/V)')
plt.grid(True)
plt.legend()
plt.show()
