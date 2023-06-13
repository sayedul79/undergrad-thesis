from skrf import Network
import matplotlib.pyplot as plt
import tikzplotlib
two_stage = Network('data/two-stage-sdb-without.s2p')
two_stage.frequency.unit = 'ghz'
fig, ax = plt.subplots(figsize=(8, 6))
two_stage.plot_s_db(0, 1, linewidth=2, color="red", label="S22")
ax.grid(True)
#ax.set_xlim(0e9, 40e9)
# ax.set_ylim(-10, 30)
ax.tick_params(axis='both', labelsize=12)
ax.set_xlabel("Frequency (GHz)", fontsize=15)
ax.set_ylabel("Magnitude (dB)", fontsize=15)
#ax.set_xlim(10e9, 40e9)
#ax.set_ylim(-80, -50)
#plt.legend().remove()
#tikzplotlib.clean_figure()
#tikzplotlib.save("two_stage_sdb_cadence_s11.tex")
#plt.savefig('two_stage_s22.png', dpi=300)
plt.show()
