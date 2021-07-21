import odrive
import time
import os
import sys
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import threading

window = Tk()
speed = 0
MAX = 3
os.system("(lsusb -d 1209:0d32 -v; lsusb -d 0483:df11 -v) | grep iSerial")

serial_number1 = '205639874D4D'
serial_number2 = '205D337F304B'

#You can list all devices connected to USB by running
#(lsusb -d 1209:0d32 -v; lsusb -d 0483:df11 -v) | grep iSerial


#my_drive0 = odrive.find_any(path="usb",serial_number="205639874D4D")
my_drive0 = odrive.find_any(path="usb",serial_number="205D337F304B")

#my_drive0 = odrive.find_any()
#odrive.find_any("usb", serial_number)

#odrv0 = odrive.serial_number(--path usb,serial:/dev/ttyUSB0) #serial_number="205D337F304B")
#odrv1 = odrive.find_any(serial_number="205639874D4D")
#odrv0 = odrive.find_any(path="usb",serial_number="205639874D4D",search_cancellation_token=None,channel_termination_token=None,timeout=3)
#odrv1 = odrive.find_any(path="usb",serial_number=serial_number2,search_cancellation_token=None,channel_termination_token=None,timeout=3)
#find_odrive_cancellation_token.set()
#axis = odrv0.axis0

#axis = odrv1.axis0
#mo = axis.motor
#enc = axis.encoder

def right_wheels(speed):
    speed = int(speed)
    my_drive0.axis0.controller.input_vel = speed
    my_drive0.axis1.controller.input_vel = speed


def stop(speed):
    my_drive0.axis0.controller.input_vel = speed
    my_drive0.axis1.controller.input_vel = speed
    #my_drive1.axis0.controller.input_vel = 0
    #my_drive1.axis1.controller.input_vel = 0


def left_wheels(speed):
    my_drive1.axis0.controller.input_vel = -speed
    my_drive1.axis1.controller.input_vel = -speed


def stop():
    speed = 0
    return speed

count = 0
def test_run():
    #global count
    count = count +1
    entry0.delete(0, END)
    entry0.insert(END, count)


#entry0 = Entry(window, width=20).grid(row=0, column=0, padx=10, pady=10)
#btn_1 = Button(window, text="test").grid(row=1, column=0)


def run_r_motor():
    pass
    def run0():
        #count = 0
        pass
        #speed = 0
        while True:
            try:
                count = entry0.get()
                right_wheels(count)
                #time.sleep(5)
                #right_wheels(stop())
                #time.sleep(2)
                #speed = count
                #right_wheels(-speed)
                #time.sleep(5)
                #right_wheels(stop())
                #count = count + 1
                #global count1
                #count1 = count
                #if count == MAX:
                #    count = 0
                #else:
                #    pass
                #speed = count
                #right_wheels(stop())
                #time.sleep(2)
                print ("count: ", count)
            except KeyboardInterrupt:
                print("Program interrupted .......")
                #time.sleep(2)
                right_wheels(stop())
                sys.exit()
    thread0 = threading.Thread(target=run0)
    thread0.start()

entry0 = Entry(window, width=20)
btn_1 = Button(window, text="Send", command=run_r_motor).grid(row=1, column=0)
btn_2 = Button(window, text="test_run", command=run_r_motor).grid(row=2, column=0)
entry0.grid(row=0, column=0, padx=10, pady=10)


#entry0.delete(0, END)
#entry0.insert(END, count1)


window.mainloop()

#odrv1.axis0.controller.input_vel = 0
#odrv0.axis0.controller.input_vel = 1
#print('Odrive ID: ', my_drive)
#print('Odrive2 ID: ', odrv1)


#find_odrive_cancellation_token)
#        find_odrive_cancellation_token.set()

#odrive.find_any("serial:/dev/ttyUSB0")
