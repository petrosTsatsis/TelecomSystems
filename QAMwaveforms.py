# import libraries to use
import commlib as cl
import matplotlib.pyplot as plt

# Parameters
TS = 1e-6
samples_per_symbol = 20
tinitial = 0
tguard = 10 * TS

# Name attribute
name = 'Petros Tsatsis'

# Convert string name to binary
bits = ''.join(format(ord(i), '08b') for i in name)

# Signal constellation for M = 4 QAM
c = cl.qam_constellation(4)

# Waveform
x = cl.digital_signal(TS=TS, samples_per_symbol=samples_per_symbol,
                      tinitial=tinitial, tguard=tguard, constellation=c)

if (len(bits) % 2 != 0):
    while (len(bits) % 2 != 0):
        bits = bits + '0'

# Create waveform with input bits
x.modulate_from_bits(bits, constellation=c)

# True for close first all plots and 1 to set the figure number
x.plot(True, 1)

# Signal constellation for M = 16 QAM
c = cl.qam_constellation(16)

# Waveform
x = cl.digital_signal(TS=TS, samples_per_symbol=samples_per_symbol,
                      tinitial=tinitial, tguard=tguard, constellation=c)

if (len(bits) % 4 != 0):
    while (len(bits) % 4 != 0):
        bits = bits + '0'

# Create waveform with input bits
x.modulate_from_bits(bits, constellation=c)

# False for not closing the plots and 2 to set the figure number
x.plot(False, 2)

# Show plots
plt.show()