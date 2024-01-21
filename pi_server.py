import subprocess
import cv2
import numpy as np
import socket
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = "yourPersonalComputerIP"
server_port = 6666
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)

capture_cmd = ['libcamera-vid', '-t', '0', '--inline', '--listen', '-o', '-', '-n', '--width', '640', '--height', '480', '--codec', 'yuv420']


process = subprocess.Popen(capture_cmd, stdout=subprocess.PIPE)

while True:

    frame_size = 640 * 480 * 3 // 2  
    frame_data = process.stdout.read(frame_size)
    if not frame_data:
        break

    yuv = np.frombuffer(frame_data, np.uint8).reshape((480 * 3 // 2, 640))
    img = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)

    ret, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
    if ret:
        x_as_bytes = pickle.dumps(buffer)
        s.sendto(x_as_bytes, (server_ip, server_port))
    else:
        print("Frame encoding failed.")


process.terminate()
s.close()
