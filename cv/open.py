from dotenv import load_dotenv, find_dotenv
import os
import json
from openai import OpenAI

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

import pvporcupine
import pyaudio
import struct
import wave
import openai

access_key = os.environ.get('PORCUPINE_API_KEY')
custom_keyword_path = 'hey-med-carousel_en_windows_v3_0_0.ppn'

porcupine = pvporcupine.create(
    access_key=access_key,
    keyword_paths=[custom_keyword_path]
)

def record_audio(duration=2, filename="output.wav"):
    """
    Record audio from the default microphone for the given duration
    and save it to the specified filename.
    """
    pa = pyaudio.PyAudio()

    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=16000,
                     input=True, frames_per_buffer=1024)

    print(f"Recording for {duration} seconds...")

    frames = []

    for _ in range(0, int(16000 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    pa.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)
        wf.writeframes(b''.join(frames))

def transcribe_audio(filename):
    """
    Transcribe the specified audio file using OpenAI's Whisper.
    """
    client = openai.OpenAI()

    with open(filename, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )

    return transcript

pa = pyaudio.PyAudio()
audio_stream = pa.open(rate=porcupine.sample_rate, channels=1,
                       format=pyaudio.paInt16, input=True,
                       frames_per_buffer=porcupine.frame_length)

print("Listening for the wake word...")

while True:
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

    if porcupine.process(pcm) >= 0:
        print("Wake word detected!")
        break

audio_stream.close()
pa.terminate()

record_audio(duration=2, filename="output.wav")
transcription = transcribe_audio("output.wav")
print(transcription)
