import socket
import subprocess
import sys
import serial
import threading

SEGGER = sys.argv[1]
SERIAL_PORT=sys.argv[2]

def serial_reader(port):
	s = socket.socket()
	s.bind("", 12346)
	s.listen(5)
	ser = serial.Serial(port, 115200, timeout=1)
	while True:
		conn, addr = s.accept()
		while True:
			data = ser.readline()
			if data:
				try:
					conn.send(data)
				except Exception:
					break

def main():
	t = threading.Thread(target=serial_reader, args=())
	t.start()
	port = 12345
	s = socket.socket()
	host = 'localhost'
	s.bind((host, port))
	s.listen(5)

	print ('Server listening....')

	while True:
		try:
			conn, addr = s.accept()     # Establish connection with client.
		except KeyboardInterrupt:
			exit()
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