import socket
import subprocess
import sys
import serial
import threading
import asyncio

SEGGER = sys.argv[1]
SERIAL_PORT=sys.argv[2]

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

async def recv_hex(reader, writer):
    filename='foo.hex'
    f = open(filename,'wb')

    while True:
        data = await reader.read(2048)
        if data:
            f.write(data)
        else:
            break
    f.close()
    cmd = "nrfjprog --program foo.hex --sectorerase --reset".split()
    subprocess.run(cmd)
    print("Done")

async def serial_send(reader, writer):
    ser = serial.Serial(SERIAL_PORT, 115200, timeout=1)
    while True:
        data = ser.readline()
        if data:
            try:
                writer.write(data)
            except Exception:
                break

def main():
    loop = asyncio.get_event_loop()
    server1 = loop.run_until_complete(asyncio.start_server(recv_hex, '127.0.0.1', 12345, loop=loop))
    server2 = loop.run_until_complete(asyncio.start_server(serial_send, '127.0.0.1', 12346, loop=loop))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        server1.close()
        server2.close()

if __name__ == '__main__':
    main()
