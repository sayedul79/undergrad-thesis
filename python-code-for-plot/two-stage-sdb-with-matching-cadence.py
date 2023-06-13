import numpy as np
from skrf import Network
import matplotlib.pyplot as plt
import tikzplotlib
two_stage = Network('data/two-stage-sdb.s2p')
two_stage.frequency.unit = 'ghz'
fig, ax = plt.subplots(figsize=(8, 6))
two_stage.plot_s_db(0, 0, linewidth=2, color="red", label="S11")

#Plot s12
# a\\x.set_xlim(20e9, 40e9)
# ax.set_ylim(-100, -30)
# # plot for s21
# ax.plot(27.12e9, 25, marker='o', markersize=5, color='black')
# ax.annotate('(27.12GHz, 25dB)', xy=(27.12e9, 25), xytext=(24.12e9, 5), arrowprops=dict(arrowstyle='->'), fontsize=12)
# ax.plot(32.33e9, 18.96, marker='o', markersize=5, color='blue')
# ax.annotate('(32.33GHz, 18.96dB)', xy=(32.33e9, 18.96), xytext=(30.33e9, 5), arrowprops=dict(arrowstyle='->', color="blue"), fontsize=12, color="blue")


#plot for s11
#ax.plot(27.12e9, -16.38, marker='o', markersize=5, color='black')
#ax.plot(32.33e9, -10.22, marker='o', markersize=5, color='black')

# freq_val=27.12e9
# mag_val=-16.38

# arrow_end = (freq_val, mag_val)
# arrow_start = (30e9, -16.38)

# # Draw the arrow
# ax.annotate('(27.12GHz, -16.38dB)', xy=arrow_end, xytext=arrow_start, arrowprops=dict(arrowstyle='->'), fontsize=12)
# ax.annotate('(32.33GHz, -10.22dB)', xy=(32.33e9, -10.22), xytext=(36e9, -11), arrowprops=dict(arrowstyle='->'), fontsize=12)
# Denote the arrow coordinates
#ax.text(2.5, 3, f'({arrow_end[0]}, {arrow_end[1]})')

#ax.text(28e9, -16.38, f'({freq_val:.2f}, {mag_val:.2f})', fontsize=12, color='red')
ax.grid(True)
#ax.set_xlim(10e9, 50e9)
ax.tick_params(axis='both', labelsize=12)
ax.set_xlabel("Frequency (GHz)", fontsize=15)
ax.set_ylabel("Magnitude (dB)", fontsize=15)
# #plt.legend().remove()
#plt.xlim(20e9, 40e9)
#plt.ylim(-100, -35)
#tikzplotlib.clean_figure()
#tikzplotlib.save("two_stage_sdb_withMatching_cadence_s11.tex")
#plt.savefig('two_stage_withMatching_s11.png', dpi=300)
plt.show()