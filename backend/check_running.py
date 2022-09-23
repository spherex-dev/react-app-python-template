import time
import socket

# a simple script to wait to block until the port is running
timeout = 10
start = time.time()
connected = False
while time.time() - start < timeout:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("localhost", 8000))
        connected = True
        break
    except ConnectionRefusedError:
        time.sleep(0.1)
        print("waiting for server")

print("Sanic server is running" if connected else "Sanic server failed to start")
