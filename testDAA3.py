import numpy as np
import matplotlib.pyplot as plt

# Generate random earthquake signal
n = 1000
t = np.linspace(0, 10, n)
amplitude = np.sin(2 * np.pi * 5 * t) * np.exp(-t / 2)
noise = np.random.normal(0, 0.1, n)
earthquake = amplitude + noise

# Compute FFT
y = np.fft.fft(earthquake)

# Plot time-domain graph
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.plot(t, earthquake)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')

# Plot frequency-domain graph
freq = np.fft.fftfreq(n, t[1] - t[0])
y_abs = np.abs(y)
ax2.stem(freq, y_abs)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude')

# Analyze earthquake signal
peak_freq = np.argmax(y_abs)
mag = round(np.log10(max(y_abs)) * 1.5 - 2, 1) # Richter scale magnitude
depth = round((peak_freq / n) * 200, 1)  # depth in km
impact = "Unknown"  # impact description
aftershocks = round(np.sum(np.abs(y_abs[peak_freq-10:peak_freq+10]))/np.max(y_abs[peak_freq-10:peak_freq+10]), 1)  # number of aftershocks
data = {"Magnitude": mag, "Depth (km)": depth, "Impact": impact, "Aftershocks": aftershocks}
table_data = list(data.items())

# Show plots
plt.tight_layout()
plt.show()

# Table with earthquake information
fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax.axis('off')
ax.axis('tight')
ax.table(cellText=table_data, colLabels=None, cellLoc='left', loc='center')
plt.show()

