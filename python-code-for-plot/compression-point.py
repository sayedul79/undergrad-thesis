import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tikzplotlib
df=pd.read_csv("data/compression_curve_two_stage.csv")
pin = np.array(df['compressionCurves X'])  # Input power levels
pout = np.array(df['compressionCurves Y'])  # Output power levels
fig, ax=plt.subplots(figsize=(8, 6))
# Plotting the data
ax.plot(pin, pout, linewidth=1.5, color="red")
ax.plot([-30, -8.145], [15.856, 15.856], color="blue", linestyle="--")
ax.plot([-8.145, -8.145], [15.856, -5], color="blue", linestyle="--")
ax.plot(-8.145, 15.856, marker='o', markersize=5, color='blue')
p1db_x=-8.145
p1db_y=15.856
ax.text(-7.5, 15.2, f'({p1db_x:.2f}, {p1db_y:.2f})', fontsize=12, color='blue', font="Times New Roman")

#ax.axhline(y=18.72, color='r', linestyle='--')
#ax.axhline(y=15.856, color='r', linestyle='--')
plt.grid()
ax.tick_params(axis='both', labelsize=12)
ax.set_xlabel('Pin (dBm)', fontsize=17)
ax.set_ylabel('Pout (dBm)', fontsize=17)
ax.set_xlim(-30, 30)
ax.set_ylim(-5, 20)

#plt.savefig('compressionCurves.png', dpi=300, transparent=True)
print("Psat is ", np.max(pout))
plt.show()