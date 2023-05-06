import math
import numpy as np
import matplotlib.pyplot as plt

def calculateDFT(len,time_sample):
    xn = time_sample
    Xr = []
    Xi = []
    N = 0

  #for i in range(len):
   #     val = int(input(f"Enter the value of x[{i}]: "))
    #    xn.append(val)'''

    N = int(input("Enter the number of points in the DFT: "))
    for k in range(N):
        Xr.append(0)
        Xi.append(0)
        for n in range(len):
            Xr[k] += xn[n] * math.cos(2 * math.pi * k * n / N)
            Xi[k] -= xn[n] * math.sin(2 * math.pi * k * n / N)

    # Plotting the time-domain graph
    t = np.linspace(0, len-1, 10*len)  # higher sampling rate
    xn_interp = np.interp(t, range(len), xn)  # interpolate for a smooth curve
    plt.subplot(2, 1, 1)
    plt.plot(t, xn_interp, 'b-')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Time-Domain Graph')

    # Plotting the frequency-domain graph
    freq = np.arange(N) / N
    mag = np.sqrt(np.square(Xr) + np.square(Xi))
    plt.subplot(2, 1, 2)
    plt.bar(freq, mag, width=1/N, align='edge')
    plt.xlabel('Normalized frequency')
    plt.ylabel('Magnitude')
    plt.title('Frequency-Domain Graph')

    plt.tight_layout()
    plt.show()

import random

sample_size = 1000
time_sample = [random.uniform(-1, 1) for _ in range(sample_size)]

calculateDFT(sample_size,time_sample)

