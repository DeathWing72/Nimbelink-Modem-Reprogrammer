import serial
import time

encoding = 'utf-8'
print("Which COM port will be used?")
port = input()
ser = serial.Serial(
    port = port,
    baudrate = 115200,
    timeout = 1)
ser.isOpen()
time.sleep(1)
ser.write("AT+CPIN?\r\n".encode(encoding))
time.sleep(1)
out = ''
read = False
while ser.inWaiting() > 0 & read == False:
    out += ser.read(1).decode(encoding)
    if out != '':
        read = True
print(out)
ser.write("AT+IPR=9600\r\n".encode(encoding))
time.sleep(1)
out = ''
read = False
while ser.inWaiting() > 0 & read == False:
    out += ser.read(1).decode(encoding)
    if out != '':
        read = True
print(out)
ser.baudrate = 9600
ser.write("AT+CPIN?\r\n".encode(encoding))
time.sleep(1)
out = ''
read = False
while ser.inWaiting() > 0 & read == False:
    out += ser.read(1).decode(encoding)
    if out != '':
        read = True
print(out)
ser.write("AT&W\r\n".encode(encoding))
time.sleep(1)
out = ''
read = False
while ser.inWaiting() > 0 & read == False:
    out += ser.read(1).decode(encoding)
    if out != '':
        read = True
print(out)
