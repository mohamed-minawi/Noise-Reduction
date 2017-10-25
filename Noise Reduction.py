import numpy
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Read the audio wave
rate, data = wavfile.read('audio.wav')
# Perfom fft
datafft = numpy.fft.rfft(data)
# Low Pass Filter with cutoff 4k
if(len(datafft)>6000):
    datafft[6000:]=0;
# Perform ifft
newdata = numpy.fft.irfft(datafft)
filteredwrite = numpy.round(newdata).astype('int16')
# Write the new audio wave
wavfile.write('newaudio.wav', rate, filteredwrite)

#Display the frequency spectrum
#y = numpy.array([float(i) for i in range(0,len(data)/2+1)])
#plt.plot(y,filtereddata)
#plt.show()
