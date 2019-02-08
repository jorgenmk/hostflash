import socket

def main():
    s = socket.socket()         # Create a socket object
    host = '10.0.2.2' # Get local machine name
    port = 12345                 # Reserve a port for your service.

    s.connect((host, port))
    f = open('zephyr/zephyr.hex','rb')
    print ('Sending...')
    s.send(f.read())
    f.close()
    s.close()

if __name__ == '__main__':
    main()