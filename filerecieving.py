import socket
from datetime import datetime
import threading
import transcription

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1532))

server_socket.listen(2)
print("Listening on port 1532")
pid = ''
while 1:
    connection, address = server_socket.accept()
    print("Accepted connection from %s" % str(address))
    filename = connection.recv(1024).decode()
    timestamp = datetime.now().strftime("%m-%d-%H-%M-%S")
    if filename.endswith(".wav"):
        filename = f"received{timestamp}.wav"
    else:
        filename = f"received{timestamp}.mp4"
    with open(filename, "wb") as file:
        while 1:
            data = connection.recv(1024)
            print(filename)
            if not data:
                thr = threading.Thread(target=transcription.transcribe, args=(filename,)).start()
                break
            file.write(data)