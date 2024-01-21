import tkinter as tk
import socket
import pickle
import cv2
import numpy as np
from threading import Thread

def send_capture_signal():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"capture", (pi_ip, pi_port))

def receive_photo():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('', laptop_port))
        while True:
            data, _ = s.recvfrom(1000000)
            photo = pickle.loads(data)
            image = cv2.imdecode(photo, cv2.IMREAD_COLOR)
            cv2.imshow('Received Photo', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

pi_ip = "127.0.0.1"
pi_port = 6666

laptop_port = 7777

def create_gui():
    root = tk.Tk()
    root.title("Camera Control")
    button = tk.Button(root, text="Capture Photo", command=send_capture_signal)
    button.pack(pady=20)
    root.mainloop()

Thread(target=receive_photo, daemon=True).start()

create_gui()
