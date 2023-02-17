import numpy as np
import sounddevice as sd
import soundfile as sf

frequency = 18500  # Frequency in Hz
sample_rate = 44100  # Sample rate in Hz
duration = 600.0  # Duration in seconds


def reverse_phase_tone(frequency, duration, sample_rate):
    # Generate a sine wave with the given frequency and duration
    t = np.linspace(0, duration, int(duration * sample_rate))
    wave = np.sin(2 * np.pi * frequency * t)

    # Reverse the phase of the wave
    wave = -wave

    return wave

# Generate a reversing phase tone with a frequency of 440 Hz and a duration of 1 second,
# sampled at 44.1 kHz
wave = reverse_phase_tone(frequency, duration, sample_rate)
# sd.play(wave)
# sd.wait()
sf.write('test_tone.wav', wave, sample_rate)

