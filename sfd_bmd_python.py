import pandas as pd

# Load the Excel file
file_path = "SFS_Screening_SFDBMD.xlsx"
xls = pd.ExcelFile(file_path)

# Display sheet names to understand the structure
xls.sheet_names

# Load the data from the first sheet
df = pd.read_excel(xls, sheet_name = "Sheet1")

# Display the first few rows of the dataset
df.head()

import matplotlib.pyplot as plt

# Extracting data for plotting
distance = df["Distance (m)"]
shear_force = df["SF (kN)"]
bending_moment = df["BM (kN-m)"]

# Create a figure with two subplots
fig, axes = plt.subplots(2, 1, figsize = (10, 8), sharex = True)

# Plot Shear Force Diagram (SFD) 
axes[0].plot(distance, shear_force, color = "blue", marker = "o", linestyle = "-", label = "Shear Force")
axes[0].axhline(0, color = "black", linewidth = 1)  # Zero line
axes[0].set_ylabel("Shear Force (kN)")
axes[0].set_title("Shear Force Diagram (SFD)")
axes[0].grid(True)
axes[0].legend()

# Plot Bending Moment Diagram (BMD)
axes[1].plot(distance, bending_moment, color = "red", marker = "s", linestyle = "-", label = "Bending Moment")
axes[1].axhline(0, color = "black", linewidth = 1)  # Zero line
axes[1].set_xlabel("Distance (m)")
axes[1].set_ylabel("Bending Moment (kN-m)")
axes[1].set_title("Bending Moment Diagram (BMD)")
axes[1].grid(True)
axes[1].legend()

# Show the plot
plt.tight_layout()
plt.show()