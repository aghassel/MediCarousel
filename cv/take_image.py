import subprocess
import socket
import pickle
import cv2
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 6666))

laptop_ip = "172.20.10.4"
laptop_port = 7777

while True:
    data, _ = s.recvfrom(1024)
    if data == b"capture":
        capture_cmd = ['libcamera-still', '-o', '-', '--width', '640', '--height', '480', '--nopreview']
        process = subprocess.Popen(capture_cmd, stdout=subprocess.PIPE)
        frame_data = process.stdout.read()
        process.terminate()

        if frame_data:
            img = np.frombuffer(frame_data, np.uint8).reshape((480, 640, 3))
            ret, buffer = cv2.imencode(".jpg", img)
            if ret:
                x_as_bytes = pickle.dumps(buffer)
                s.sendto(x_as_bytes, (laptop_ip, laptop_port))
            else:
                print("Frame encoding failed.")

s.close()
