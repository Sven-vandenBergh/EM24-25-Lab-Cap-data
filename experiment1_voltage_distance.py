#import all necessary modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#------------------------------#
#-----2mm----------------------#
#------------------------------#

# Charge transfer steps
charge_steps = np.arange(1, 10)

# Voltage measurements for 2mm plate separation
voltage_2mm = np.array([
    [12, 10, 11],
    [20, 20, 25],
    [28, 25, 35],
    [39, 35, 48],
    [48, 45, 59],
    [57, 62, 65],
    [69, 71, 75],
    [75, 82, 83],
    [94, np.nan, np.nan]
])

# mean voltage and standard deviation (ignoring NaN values)
avg_voltage_2mm = np.nanmean(voltage_2mm, axis=1)
std_voltage_2mm = np.nanstd(voltage_2mm, axis=1)

#charge_steps to match the length of avg_voltage_2mm
charge_steps_trimmed = charge_steps[:len(avg_voltage_2mm)]

# Linear regression for best-fit line
slope_2mm, intercept_2mm, r_value, _, _ = linregress(charge_steps_trimmed, avg_voltage_2mm)
print(f"2mm Plate Separation:")
print(f"  Slope = {slope_2mm:.2f} V per step")
print(f"  y-intercept = {intercept_2mm:.2f} V")
print(f"  R-squared = {r_value**2:.3f}")

# best-fit line
fit_2mm = slope_2mm * charge_steps_trimmed + intercept_2mm

#error bars
plt.figure(figsize=(8, 6))
plt.errorbar(charge_steps_trimmed, avg_voltage_2mm, yerr=std_voltage_2mm,
             fmt='o', label='2mm Plate Separation', color='darkslategrey', capsize=5)
plt.plot(charge_steps_trimmed, fit_2mm, linestyle='--', color='darkslategrey', label='Best Fit Line')

#formula
formula = rf"$V = {slope_2mm:.2f}Q + {intercept_2mm:.2f}$"
plt.text(2, max(avg_voltage_2mm) - 15, formula, fontsize=12, color="darkslategrey")  # Adjusted y-position

plt.xlabel("Charge Transfer Steps")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs. Charge Transfer Steps (2mm Separation)")
plt.legend()
plt.grid()
plt.show()

# Charge transfer steps (trimmed to match valid data)
charge_steps = np.arange(1, 6)  # Steps 1–5 (since steps 6–9 are NaN)

# Voltage measurements for 4mm plate separation (trimmed to exclude NaN rows)
voltage_4mm = np.array([
    [23, 25, 25],
    [42, 41, 45],
    [60, 58, 55],
    [72, 75, 66],
    [84, 89, 85]
])

#------------------------------#
#-----4mm----------------------#
#------------------------------#


#mean voltage and standard deviation
avg_voltage_4mm = np.nanmean(voltage_4mm, axis=1)
std_voltage_4mm = np.nanstd(voltage_4mm, axis=1)

# Linear regression for best-fit line
slope_4mm, intercept_4mm, r_value, _, _ = linregress(charge_steps, avg_voltage_4mm)
print("4mm Plate Separation:")
print(f"  Slope = {slope_4mm:.2f} V per step")
print(f"  y-intercept = {intercept_4mm:.2f} V")
print(f"  R-squared = {r_value**2:.3f}")

# best-fit line
fit_4mm = slope_4mm * charge_steps + intercept_4mm

#error bars
plt.figure(figsize=(8, 6))
plt.errorbar(charge_steps, avg_voltage_4mm, yerr=std_voltage_4mm,
             fmt='o', label='4mm Plate Separation', color='salmon', capsize=5)
plt.plot(charge_steps, fit_4mm, linestyle='--', color='salmon', label='Best Fit Line')
formula = rf"$V = {slope_4mm:.2f}Q + {intercept_4mm:.2f}$"
plt.text(1.5, max(avg_voltage_4mm) - 15, formula, fontsize=12, color="salmon")  # Adjust position as needed

plt.xlabel("Charge Transfer Steps")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs. Charge Transfer Steps (4mm Separation)")
plt.legend()
plt.grid()
plt.show()

#------------------------------#
#-----combined-----------------#
#------------------------------#

# Best-fit lines
fit_2mm = slope_2mm * charge_steps_trimmed + intercept_2mm
fit_4mm = slope_4mm * charge_steps + intercept_4mm

# Create a single figure
plt.figure(figsize=(8, 6))
plt.rc('text', usetex=False)
plt.rc('font', family='serif')

# Plot 2mm separation data
plt.errorbar(charge_steps_trimmed, avg_voltage_2mm, yerr=std_voltage_2mm,
             fmt='o', label='2mm Plate Separation', color='darkslategrey', capsize=5)
plt.plot(charge_steps_trimmed, fit_2mm, linestyle='--', color='darkslategrey', label='Best Fit Line (2mm)')

# Plot 4mm separation data
plt.errorbar(charge_steps, avg_voltage_4mm, yerr=std_voltage_4mm,
             fmt='o', label='4mm Plate Separation', color='salmon', capsize=5)
plt.plot(charge_steps, fit_4mm, linestyle='--', color='salmon', label='Best Fit Line (4mm)')

# Add formulas
formula_2mm = rf"$V = {slope_2mm:.2f}Q + {intercept_2mm:.2f}$"
formula_4mm = rf"$V = {slope_4mm:.2f}Q + {intercept_4mm:.2f}$"

# Position text annotations dynamically
plt.annotate(formula_2mm, xy=(min(charge_steps_trimmed), max(avg_voltage_2mm) * 0.9),
             fontsize=12, color="darkslategrey")
plt.annotate(formula_4mm, xy=(min(charge_steps), max(avg_voltage_4mm) * 0.8),
             fontsize=12, color="salmon")

# Labels and formatting
plt.xlabel(r"Charge Transfer Steps ($Q$)")
plt.ylabel(r"Voltage ($V$)")
plt.title("Voltage vs. Charge Transfer Steps for Different Plate Separations")
plt.legend()
plt.grid()

# Show the plot
plt.show()

