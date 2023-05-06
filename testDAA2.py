import math
import numpy as np
import matplotlib.pyplot as plt

def FFT(x):
    n = len(x)
    if n == 1:
        return x
    x_odd = x[1::2]
    x_even = x[::2]
    y_odd = FFT(x_odd)
    y_even = FFT(x_even)
    w_n = math.e ** (-2j * math.pi / n)
    y = [0] * n
    for j in range(n//2):
        y[j] = y_even[j] + w_n**j * y_odd[j]
        y[j + n//2] = y_even[j] + w_n**(j + n//2) * y_odd[j]
    return y

import random

sample_size = 1000
time_sample = [random.uniform(-1, 1) for _ in range(sample_size)]

# Compute FFT
y = FFT(time_sample)

# Plot time-domain graph
plt.subplot(2, 1, 1)
plt.plot(sample_size, time_sample)
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Plot frequency-domain graph
freq = np.fft.fftfreq(len(x), t[1] - t[0])
y_abs = np.abs(y)
plt.subplot(2, 1, 2)
plt.stem(freq, y_abs)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.show()
