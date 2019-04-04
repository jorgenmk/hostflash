import serial

def main():
    ser = serial.Serial('/tmp/testACM0', timeout=1)
    while True:
        data = ser.readline()
        if data:
            print(data.decode().strip())

main()
