import cv2
import socket
import pickle
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import threading
import base64
import requests
import os
from pathlib import Path
from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
import os
import json
from openai import OpenAI

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
access_key = os.environ.get('PORCUPINE_API_KEY')

# Function to encode image to base64
def encode_image(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to get instrument status using OpenAI's API
def get_instrument_status(image_path):
    base64_image = encode_image(image_path)
    api_key = os.environ.get('OPENAI_API_KEY')

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What colour marker do you see in the image? If it is blue, say scalpel ready. If it is orange say dirty instrument, please steralize. If it is brown, say scissors ready. If you see the back of the marker say instrument incorrectly oriented."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "med"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 100
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    try:
        response_json = response.json()
        instrument_status = response_json.get('choices', [])[0].get('message', {}).get('content', '')
        return instrument_status
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to speak a message using OpenAI's text-to-speech
def speak_message(message):
    client = OpenAI()

    try:
        base_path = Path(__file__).parent
    except NameError:
        base_path = Path.cwd()

    speech_file_path = base_path / "response.mp3"

    response = client.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input=message
    )

    response.stream_to_file(speech_file_path)

    if os.name == 'nt':  # Windows
        os.system(f"start {speech_file_path}")
    elif os.name == 'posix':  # macOS, Linux, Unix, etc.
        os.system(f"open {speech_file_path}")

# Function to capture and analyze the image
def capture_image():
    global frame
    if frame is not None:
        cv2.imwrite("captured_image.jpg", frame)
        status = get_instrument_status("captured_image.jpg")
        if "properly" in status and "sterile" in status:
            speak_message("MediCarousel is ready")
        else:
            speak_message(status)
    else:
        print("No frame to capture.")

# Function to continuously update the video stream in the GUI
def video_stream(label):
    global frame
    while True:
        packet, addr = s.recvfrom(65536)  # Buffer size is 65536 bytes
        data = pickle.loads(packet)
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

        if frame is not None:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.config(image=imgtk)
        else:
            print("Failed to decode frame.")

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = "0.0.0.0"  # Listen on all interfaces
server_port = 6666
s.bind((server_ip, server_port))
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1000000)

# Setting up the GUI
root = tk.Tk()
root.title("Camera Stream")
root.geometry("800x600")

frame_label = tk.Label(root)
frame_label.pack()

capture_button = tk.Button(root, text="Capture Image", command=capture_image)
capture_button.pack()

# Start the video stream in a separate thread
thread = threading.Thread(target=video_stream, args=(frame_label,))
thread.daemon = 1
thread.start()

root.mainloop()
s.close()
