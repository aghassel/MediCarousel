import cv2
import socket
import pickle
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_ip = "0.0.0.0"
server_port = 6666
s.bind((server_ip, server_port))


s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1000000)

print(f"Server listening on {server_ip}:{server_port}")

try:
    while True:
        packet, addr = s.recvfrom(65536) 
        data = pickle.loads(packet)

        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

        if frame is not None:
            cv2.imshow("Received Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
        else:
            print("Failed to decode frame.")
except Exception as e:
    print(f"Error: {e}")
finally:
    cv2.destroyAllWindows()
    s.close()