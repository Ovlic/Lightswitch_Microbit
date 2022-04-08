import serial, subprocess, time
from os.path import exists

def printred(msg):
    print(f"{bold[0]}{red[0]}{msg}{red[1]}{bold[1]}")

def printgreen(msg):
    print(f"{bold[0]}{green[0]}{msg}{green[1]}{bold[1]}")

def printyellow(msg):
    print(f"{bold[0]}{yellow[0]}{msg}{yellow[1]}{bold[1]}")


class CannotOpenPort(Exception):
    "Raised when the specified serial port doesn't exist"

    def __init__(self, message="Cannot open port. Is microbit connected?"):
        self.message = message
    
    def __str__(self):
        return self.message


class Disconnected(Exception):
    "Raised when the microbit is disconnected"

    def __init__(self, message="Microbit disconnected."):
        self.message = message

    def __str__(self):
        return self.message


port = "/dev/cu.usbmodem14102" # Change if needed; use 'ls /dev/cu.*' and look for '/dev/cu.usbmodem'
baud = 115200

if not exists(port):
    raise CannotOpenPort()

s = serial.Serial(port)
s.baudrate = baud

try:
    while True:
        if not exists(port):
            raise CannotOpenPort()

        raw_data = s.readline()
        data = raw_data.decode('utf-8')
        data = ' '.join(data.split())
        #print(f"Data: '{data}'")

        if data == "light_on":
            printgreen("Light On")
            f = open("light_on.applescript", "r")
            data = f.read()
            f.close()
            subprocess.call(['osascript', '-e', data])

            
        elif data == "light_off":
            printred("Light Off")
            f = open("light_off.applescript", "r")
            data = f.read()
            f.close()
            subprocess.call(['osascript', '-e', data])
            

except KeyboardInterrupt:
    print("\nExiting...")
    s.close()
    print("Exited.")

except OSError:
    print("oserror")
    s.close()
    raise Disconnected()

except serial.serialutil.SerialException:
    print("serial exception")
    s.close()
    raise

