import pyaudio
from flask import Flask, Response

# Flask App
app = Flask(__name__)

# Audio Configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

audio = pyaudio.PyAudio()

# Open Audio Stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

@app.route('/stream')
def audio_stream():
    def generate():
        while True:
            data = stream.read(CHUNK)
            yield data

    return Response(generate(), mimetype="audio/x-wav")

if __name__ == '__main__':
    print("Starting audio stream server...")
    app.run(host='0.0.0.0', port=5000)
