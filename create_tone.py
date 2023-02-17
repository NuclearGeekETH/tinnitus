import wave
import struct
import math

frequency = 17000    # Hz
duration = 10       # seconds
sample_rate = 44100   # samples per second

num_samples = duration * sample_rate

wave_file = wave.open('tone.wav', 'w')
wave_file.setnchannels(1)  # 1 channel for mono
wave_file.setsampwidth(2)  # 2 bytes per sample
wave_file.setframerate(sample_rate)

for i in range(num_samples):
    value = int(32767.0*math.sin(frequency*math.pi*float(i)/float(sample_rate)))
    data = struct.pack('<h', value)
    wave_file.writeframes(data)

wave_file.close()
