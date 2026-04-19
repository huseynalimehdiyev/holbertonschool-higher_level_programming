#!/usr/bin/python3
"""Shebang"""

import socket
import json


HOST = "127.0.0.1"
PORT = 65432


def start_server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((HOST, PORT))
            server.listen(1)

            conn, addr = server.accept()
            with conn:
                data = conn.recv(4096)

                if data:
                    received_dict = json.loads(data.decode("utf-8"))
                    print("Received Dictionary from Client:")
                    print(received_dict)

    except Exception:
        pass


def send_data(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))

            serialized_data = json.dumps(data).encode("utf-8")
            client.sendall(serialized_data)

    except Exception:
        pass
