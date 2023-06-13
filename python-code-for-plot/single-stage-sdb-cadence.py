from skrf import Network
import matplotlib.pyplot as plt
import tikzplotlib
tikzplotlib.Flavors.context.preamble()
single_stage = Network('data/sdb-single.s2p')
single_stage.frequency.unit = 'ghz'
fig, ax = plt.subplots(figsize=(8, 6))
single_stage.plot_s_db(1, 1, linewidth=2, color="red", label="S22")
ax.grid(True)
#ax.set_ylim(-30, 5)
#ax.set_ylim(-120, -25) for s12
ax.tick_params(axis='both', labelsize=12)
ax.set_xlabel("Frequency (GHz)", fontsize=15)
ax.set_ylabel("Magnitude (dB)", fontsize=15)
#plt.legend().remove()
#tikzplotlib.clean_figure()
#tikzplotlib.save("single_stage_sdb_cadence_s11.tex")
#plt.savefig('single_stage_s22.png', dpi=300)
plt.show()
