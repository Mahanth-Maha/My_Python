import numpy as np
import pyaudio
import sys

def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return amplitude * np.sin(2 * np.pi * freq * t)

def play_wave(stream, data, sample_rate):
    # Ensure the wave data is in the correct format
    wave_data = (data * 32767).astype(np.int16).tobytes()
    stream.write(wave_data)



def play(duration = 10, frequency = 40 ):
    p = pyaudio.PyAudio()

    # Stream setup
    sample_rate = 44100
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    sine_wave = generate_sine_wave(frequency, duration, sample_rate)
    play_wave(stream, sine_wave, sample_rate)

    # Cleanup
    stream.stop_stream()
    stream.close()
    p.terminate()
    
if __name__ == '__main__':
    if(len(sys.argv) > 1 and sys.argv[1] in ('-s','-t')):
        print(f"playing 40 hz for {sys.argv[2]} seconds")
        play(int(sys.argv[2]))
    elif(len(sys.argv) > 1 and sys.argv[1] == '-m'):
        print(f"playing 40 hz for {sys.argv[2]} minutes")
        play(int(sys.argv[2])*60)
    else :
        print("USAGE : python 40hzFrequencyPlay [-s SECONDS / -m MINUTES]")
        print("playing 40 hz for 10 seconds")
        play()