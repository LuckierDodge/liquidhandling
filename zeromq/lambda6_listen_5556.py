"""
Lambda6 listens for data files from the Hidex (Port 5555)
    sample sheet (csv)
    hidex data (excel or csv?)

    - lambda6 should only ever receieve data from hudson01 
        (eventually need to account for different message types, messages from hudson02?)

"""

import os
import sys
import zmq
import time
import json
from subprocess import Popen
from lambda6_handle_message_5556 import lambda6_handle_message

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    message = socket.recv()
    decoded = message.decode("utf-8")

    if message == b"SHUTDOWN":
        socket.send(b"Shutting down")
        break

    else:
        # immediately pass the message off to message handler and keep listening
        print(f"sending decoded_message: {decoded}")
        child_message_handler = Popen(
            ["python", "./lambda6_handle_message_5556.py", decoded],
            start_new_session=True,
        ).pid
        socket.send(b"Message received and passed to lambda6_handle_message")
