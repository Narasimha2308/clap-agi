import pyaudio
import numpy as np
import time
import webbrowser

# ==============================
# SETTINGS
# ==============================

THRESHOLD = 3000          # Increase if too sensitive, decrease if not detecting
MIN_DELAY = 0.2           # Minimum gap between claps (seconds)
MAX_DELAY = 1.0           # Maximum gap for a double clap (seconds)
COOLDOWN = 10             # Seconds before another activation

YOUTUBE_URL = "https://www.youtube.com/@cristiano"

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# ==============================
# AUDIO SETUP
# ==============================

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

print("=" * 50)
print("👏 Double Clap Detector Started")
print("Listening... Press Ctrl+C to stop.")
print("=" * 50)

last_clap_time = 0
clap_count = 0
last_activation = 0

try:
    while True:

        data = stream.read(CHUNK, exception_on_overflow=False)
        audio = np.frombuffer(data, dtype=np.int16)

        peak = np.abs(audio).max()

        current_time = time.time()

        # Ignore detections during cooldown
        if current_time - last_activation < COOLDOWN:
            continue

        if peak > THRESHOLD:

            time_since_last = current_time - last_clap_time

            if time_since_last > MIN_DELAY:

                if time_since_last < MAX_DELAY:
                    clap_count += 1
                else:
                    clap_count = 1

                last_clap_time = current_time

                print(f"👏 Clap detected! Count = {clap_count}")

                if clap_count == 2:

                    print("\n✅ DOUBLE CLAP CONFIRMED!")
                    print("🚀 Launching workspace...\n")

                    # Open YouTube
                    webbrowser.open(YOUTUBE_URL)

                    # Reset
                    clap_count = 0
                    last_activation = time.time()

                    print(f"Cooldown for {COOLDOWN} seconds...\n")

except KeyboardInterrupt:
    print("\nStopping...")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Program closed successfully.")