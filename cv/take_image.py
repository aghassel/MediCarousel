import asyncio
import socket
import subprocess
import cv2
import numpy as np
import pickle

async def capture_and_send_photo(reader, writer):
    # Capture a photo using libcamera-still
    capture_cmd = ['libcamera-still', '-o', '-', '--width', '640', '--height', '480', '--nopreview']
    process = subprocess.Popen(capture_cmd, stdout=subprocess.PIPE)
    frame_data = process.stdout.read()
    process.terminate()

    if frame_data:
        img = np.frombuffer(frame_data, np.uint8).reshape((480, 640, 3))
        ret, buffer = cv2.imencode(".jpg", img)
        if ret:
            x_as_bytes = pickle.dumps(buffer)
            writer.write(x_as_bytes)
            await writer.drain()
        else:
            print("Frame encoding failed.")

async def main():
    server = await asyncio.start_server(
        capture_and_send_photo, '0.0.0.0', 6666)

    async with server:
        await server.serve_forever()

asyncio.run(main())
