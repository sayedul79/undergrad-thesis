from skrf import Network
import matplotlib.pyplot as plt
import tikzplotlib
main_stage = Network('data/main_stage.s2p')
main_stage.frequency.unit = 'ghz'
main_stage.plot_s_db(1,0)
plt.show()