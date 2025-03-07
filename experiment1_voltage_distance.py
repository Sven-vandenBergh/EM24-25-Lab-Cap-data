import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from matplotlib.lines import Line2D

# Process 2mm Plate Separation Data
charge_steps_2mm = np.arange(1, 10)  # Steps 1–9
voltage_2mm = np.array([
    [0.5, 1, 1.5],
    [2, 2.3, 2],
    [3, 4, 3],
    [4.4, 4.5, 4],
    [5.2, 5, 5.2],
    [6, 6, 6.5],
    [7.2, 7, 7.5],
    [8.2, 8.3, 8.4],
    [9.5, 9, 9.5]
])

avg_voltage_2mm = np.nanmean(voltage_2mm, axis=1)
std_voltage_2mm = np.nanstd(voltage_2mm, axis=1)

slope_2mm, intercept_2mm, r_value_2mm, _, _ = linregress(charge_steps_2mm, avg_voltage_2mm)
fit_2mm = slope_2mm * charge_steps_2mm + intercept_2mm
formula_2mm = rf"2mm: $V = {slope_2mm:.2f}Q + {intercept_2mm:.2f}$"

# Process 4mm Plate Separation Data
charge_steps_4mm = np.arange(1, 12)  # Steps 1–11
voltage_4mm = np.array([
    [2.7, 1.8, 2.7],
    [4.5, 4.2, 4.5],
    [6.3, 6.0, 6.0],
    [9.0, 7.5, 7.5],
    [10.5, 9.0, 9.6],
    [12.0, 10.5, 11.4],
    [13.5, 12.0, 12.6],
    [15.0, 13.2, 14.7],
    [16.5, 13.8, 15.9],
    [17.4, 15.9, 17.4],
    [18.0, 17.7, 18.9]
])

avg_voltage_4mm = np.nanmean(voltage_4mm, axis=1)
std_voltage_4mm = np.nanstd(voltage_4mm, axis=1)

slope_4mm, intercept_4mm, r_value_4mm, _, _ = linregress(charge_steps_4mm, avg_voltage_4mm)
fit_4mm = slope_4mm * charge_steps_4mm + intercept_4mm
formula_4mm = rf"4mm: $V = {slope_4mm:.2f}Q + {intercept_4mm:.2f}$"

# Create Combined Plot
plt.figure(figsize=(10, 6))

# Plot 2mm data with error bars and best-fit line
plt.errorbar(charge_steps_2mm, avg_voltage_2mm, yerr=std_voltage_2mm, 
             fmt='o', color='blue', capsize=5, label='_nolegend_')
plt.plot(charge_steps_2mm, fit_2mm, '--', color='blue', label='_nolegend_')

# Plot 4mm data with error bars and best-fit line
plt.errorbar(charge_steps_4mm, avg_voltage_4mm, yerr=std_voltage_4mm, 
             fmt='o', color='red', capsize=5, label='_nolegend_')
plt.plot(charge_steps_4mm, fit_4mm, '--', color='red', label='_nolegend_')

# Add regression formulas
plt.text(0.05, 0.95, formula_2mm, transform=plt.gca().transAxes, 
         color='blue', fontsize=12, va='top')
plt.text(0.05, 0.88, formula_4mm, transform=plt.gca().transAxes, 
         color='red', fontsize=12, va='top')

# Custom legend with combined markers and lines
legend_elements = [
    Line2D([0], [0], color='blue', marker='o', linestyle='--', label='2mm Data and Fit'),
    Line2D([0], [0], color='red', marker='o', linestyle='--', label='4mm Data and Fit')
]
plt.legend(handles=legend_elements, loc='lower right')

# Labels and title
plt.xlabel("Charge Transfer Steps")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs. Charge Transfer Steps for 2mm and 4mm Plate Separations")
plt.grid(True)

plt.show()

# Output regression results
print("2mm Plate Separation Results:")
print(f"  Slope: {slope_2mm:.2f} V/step, Intercept: {intercept_2mm:.2f} V, R²: {r_value_2mm**2:.3f}")
print("\n4mm Plate Separation Results:")
print(f"  Slope: {slope_4mm:.2f} V/step, Intercept: {intercept_4mm:.2f} V, R²: {r_value_4mm**2:.3f}")
