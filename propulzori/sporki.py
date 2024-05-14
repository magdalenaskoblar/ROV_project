import serial
import time
import serial.tools.list_ports
import pygame
from pprint import pprint
from pySerialTransfer import pySerialTransfer
#import pyserial


pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nema dostupnih joystick uređaja.")
    pygame.quit()
    exit()

# Inicijalizacija prvog joysticka
joystick = pygame.joystick.Joystick(0)
joystick.init()

ports = serial.tools.list_ports.comports()
serial_inst = serial.Serial()
ports_list = []

for port in ports:
    ports_list.append(str(port))
    print(str(port))
       

port = 'COM6'
baud = 9600
sts = pySerialTransfer.SerialTransfer(port, baud)
sts.open()

while True:
    front =1500
    left = 1500
    right=1500
    up = 1500
    down = 1500
    pygame.event.pump()
    for i in range(joystick.get_numaxes()):
        axis = joystick.get_axis(i)
        #pprint(f"Axis {i} value: {axis:>6.3f}")

        if (i == 1):
            front = (int) (1500 + axis * -500)        
        elif (i == 0):
            if (axis <= 0):
                left = (int)( 1500 -axis * 500) 
                right = (int)(1500)
                
            elif (axis >= 0):
                right =(int)(1500 + axis * 500) 
                left = (int)(1500)
            
    buttons = joystick.get_numbuttons() 
    for i in range(joystick.get_numbuttons()):
        button = joystick.get_button(i)
        #pprint(f"num od {i} but: {butic:>6.3f}")
        if ((i == 4) & (button == 1)):
            up = (int) (1800)
        elif ((i == 5) & (button == 1)):
            down = (int) (1200)
             
    Speed = [front, left, right, up, down]
    print("Sending Speed:", Speed)
    sts.tx_obj(Speed)
    sts.send(len(Speed) * 4)

    time.sleep(0.02)
        

if _name_ == "_main_":
    main()
    pygame.quit()
    ser.close()