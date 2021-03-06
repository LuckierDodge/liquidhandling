from utils.manifest import generateFileManifest
from utils.archive import archive
import argparse
import json
import zmq
import time
import os
import sys


def lamdba6_send_instructions(instructions_dir):

    # * connect to port on hudson01
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://hudson01.bio.anl.gov:5556")

    if os.path.isdir(instructions_dir):
        instruction_files = os.listdir(instructions_dir)

        # if there are files to send
        if len(instruction_files) > 0:

            # message address = Protocol details and timestamp
            address = os.path.basename(instructions_dir)
            print(f"Address: {address}")

            # create manifest
            data = {}
            for f in instruction_files:
                f_path = os.path.join(instructions_dir, os.path.basename(f))
                tmp = generateFileManifest(f_path, "instructions")
                for key, value in tmp.items():
                    data[key] = value

            # Send message to queue
            socket.send_string(address + "***" + json.dumps(data))
            print("Message sent to port 5556 on hudson01")

            repl = socket.recv()
            print(f"Got {repl}")

            # archive instructions once sent correctly
            archive([instructions_dir], "/lambda_stor/data/hudson/instructions/")

    socket.close()


def main(args):
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--dir", help="Directory to send", required=True, type=str
    )
    args = vars(parser.parse_args())
    print("directory sent = {}".format(args["dir"]))

    instructions_dir = args["dir"]  # full path
    lamdba6_send_instructions(instructions_dir)


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)
