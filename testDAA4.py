import numpy as np
import matplotlib.pyplot as plt

# Generate random signal for nuclear explosion detection
n = 1000
t = np.linspace(0, 10, n)
amplitude = np.sin(2 * np.pi * 50 * t) * np.exp(-t / 0.5)
noise = np.random.normal(0, 0.1, n)
nuclear_explosion = amplitude + noise

# Compute FFT
y = np.fft.fft(nuclear_explosion)

# Plot time-domain graph
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.plot(t, nuclear_explosion)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')

# Plot frequency-domain graph
freq = np.fft.fftfreq(n, t[1] - t[0])
y_abs = np.abs(y)
ax2.stem(freq, y_abs)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude')

# Analyze signal for nuclear explosion detection
peak_freq = np.argmax(y_abs)
impact = "Detected" if freq[peak_freq] > 10 else "Unknown" # Check for high-frequency components
if impact == "Detected":
    print("Detected underground nuclear explosion!")
    print("Reason: High-frequency components present in signal")
else:
    print("No underground nuclear explosion detected.")



# Show plots
plt.tight_layout()
plt.show()
