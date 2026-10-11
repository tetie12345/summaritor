import asyncio
import socket

def open_connection(host, port):
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.connect((host, port))
    return server_connection

async def send_file(server_connection, filename):
    server_connection.send(filename.encode())
    server_connection.send(open(filename, "rb").read())

if __name__ == "__main__":
    connection = open_connection("localhost", 1532)
    asyncio.run(send_file(connection, "output.wav"))
    print("done")
    asyncio.run(send_file(connection, "output.mp4"))
    print("done2")