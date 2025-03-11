import numpy as np
import matplotlib.pyplot as plt

# Data for each plate separation; replace the sample numbers with your actual data.
data_sets = {
    "4cm": {
        "Center": [3.3, 2.4, 2.7],
        "Middle": [3.6, 3.3, 3.0],
        "Edge": [6.0, 5.7, 5.7]
    },
    "6cm": {
        "Center": [3.5, 3.4, 3.6],
        "Middle": [3.8, 3.7, 3.9],
        "Edge": [6.2, 6.1, 6.3]
    },
    "8cm": {
        "Center": [3.8, 3.7, 3.9],
        "Middle": [4.1, 4.0, 4.2],
        "Edge": [6.5, 6.4, 6.6]
    },
    "10cm": {
        "Center": [4.1, 4.0, 4.2],
        "Middle": [4.4, 4.3, 4.5],
        "Edge": [6.8, 6.7, 6.9]
    },
    "12cm": {
        "Center": [4.4, 4.3, 4.5],
        "Middle": [4.7, 4.6, 4.8],
        "Edge": [7.1, 7.0, 7.2]
    }
}

# Radial positions for "Center", "Middle", and "Edge" (in cm)
positions_cm = [0, 5, 10]

# Choose distinct colors for each plate separation
colors = {
    "4cm": "blue",
    "6cm": "green",
    "8cm": "red",
    "10cm": "purple",
    "12cm": "orange"
}

plt.figure(figsize=(10, 6))

# Loop through each dataset
for key, dataset in data_sets.items():
    # Calculate the average and standard deviation at each radial position
    avg_voltages = [np.nanmean(dataset[pt]) for pt in ["Center", "Middle", "Edge"]]
    std_voltages = [np.nanstd(dataset[pt], ddof=1) for pt in ["Center", "Middle", "Edge"]]
    
    # Perform a quadratic fit (degree 2 polynomial) for the dataset
    coefficients = np.polyfit(positions_cm, avg_voltages, 2)
    poly = np.poly1d(coefficients)
    x_fit = np.linspace(positions_cm[0], positions_cm[-1], 100)
    y_fit = poly(x_fit)
    
    # Plot the data with error bars (using markers)
    plt.errorbar(positions_cm, avg_voltages, yerr=std_voltages, fmt='o', color=colors[key],
                 capsize=5, label=f'{key} Data')
    # Plot the quadratic fit as a dashed line
    plt.plot(x_fit, y_fit, '--', color=colors[key])
    
plt.xlabel("Radial Position from Center (cm)")
plt.ylabel("Voltage (V)")
plt.title("Charge Density Distribution for Different Plate Separations")
plt.xticks(positions_cm)
plt.grid(True)
plt.legend()
plt.show()
