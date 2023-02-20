import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
SERVER_HOST = "local host"
SERVER_PORT = 5001

def sendfile():
    s = socket.socket()
    host = "192.168.56.1"
    port = 5001
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected to ", host)
    filename = input("File to Transfer : ")
    filesize = os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    # file = open(filename, 'wb')

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True,
                         unit_divisor=1024)
    with open(filename, "rb") as f:
        tim = 0
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:break
            s.sendall(bytes_read)
            progress.update(len(bytes_read)) # updates progress bar

    s.close()


if __name__ == '__main__':
    sendfile()
