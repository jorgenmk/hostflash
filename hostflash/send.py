import socket
import sys

def flash(hexfile):
    s = socket.socket()         # Create a socket object
    host = '10.0.2.2' # Get local machine name
    port = 12345                 # Reserve a port for your service.

    s.connect((host, port))
    f = open(hexfile,'rb')
    print ('Sending...')
    s.send(f.read())
    f.close()
    s.close()


def main():
    if len(sys.argv) == 1:
        flash('zephyr/zephyr.hex')
    else:
        flash(sys.argv[1])

if __name__ == '__main__':
    flash('zephyr/zephyr.hex')