import socket
import subprocess
import sys

SEGGER = sys.argv[1]

def main():
	port = 12345                    # Reserve a port for your service.
	s = socket.socket()             # Create a socket object
	host = 'localhost'     # Get local machine name
	s.bind((host, port))            # Bind to the port
	s.listen(5)                     # Now wait for client connection.

	print ('Server listening....')

	while True:
		conn, addr = s.accept()     # Establish connection with client.
		print ('Got connection from', addr)

		filename='foo.hex'
		f = open(filename,'wb')

		while True:
			data = conn.recv(1024)
			if data:
				f.write(data)
			else:
				break
		f.close()
		cmd = "nrfjprog -f nrf91 --program foo.hex --sectorerase --reset".split()
		subprocess.run(cmd)
		print("Done")
		conn.close()

if __name__ == '__main__':
    main()