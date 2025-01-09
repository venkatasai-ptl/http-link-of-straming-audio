import pyaudio

# Audio Configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open Audio Stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Audio stream started...")

try:
    while True:
        data = stream.read(CHUNK)
        # For now, just print the raw audio length to verify the stream is working
        print(f"Captured {len(data)} bytes of audio data.")
except KeyboardInterrupt:
    print("Stopping audio stream...")
    stream.stop_stream()
    stream.close()
    audio.terminate()
