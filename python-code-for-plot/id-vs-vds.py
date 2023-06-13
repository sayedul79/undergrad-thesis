import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
df_id=pd.read_csv("data/id-vs-vds.csv")
df_id=df_id.rename(columns={'/V0/PLUS X': "vds", '/V0/PLUS Y': "id"})
fig, ax=plt.subplots()
ax.plot(df_id["vds"], df_id["id"]*-1, color="red")
ax.plot(3.6, 56.7575E-3, marker='o', markersize=5)

ax.annotate('(3.6V, 56.76mA)', xy=(3.6, 56.7575e-3), xytext=(3.2, 50E-3), arrowprops=dict(arrowstyle='->'))
ax.grid(True)
ax.set_xlabel(r"$V_{DD}$ (V)", fontsize=15)
ax.set_ylabel(r"$I_D$ (mA)", fontsize=15)
# Define the custom formatter function
def y_formatter(value, _):
    value *= 1000  # Multiply the value by 1000
    return f'{value:.1f}'  # Use decimal notation for larger values


# Set the custom formatter function for the y-axis ticks
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(y_formatter))
ax.tick_params(axis='both', labelsize=12)
plt.savefig('id-vs-vds.png', dpi=300, transparent=True)

plt.show()