import skrf
import numpy as np
import matplotlib.pyplot as plt

# Load S-parameters from Touchstone file
ntwk = skrf.network.Network('data/two-stage-sdb.s2p')

# Convert to frequency-domain
ntwk.frequency.unit = 'ghz'
freq = ntwk.frequency.f
s = ntwk.s

# Calculate group delay
w = 2 * np.pi * freq
s21 = s[1, 0, :]
gd = -np.diff(np.unwrap(np.angle(s21))) / np.diff(w)
gd = np.insert(gd, 0, gd[0])  # Duplicate first value to keep array length

# Plot group delay
plt.plot(freq, gd)
plt.xlim(25e9, 35e9)
plt.xlabel('Frequency (GHz)')
plt.ylabel('Group Delay (ns)')
plt.show()
