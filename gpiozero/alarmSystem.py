from SimpleMFRC522 import SimpleMFRC522
from gpiozero import MotionSensor
from gpiozero import Buzzer
from gpiozero import LED
import LCD as lcd
import time
import sys

# ---Hardware Setup---
mot = MotionSensor(17)
red0 = LED(21)
red1 = LED(13)
green0 = LED(5)
lcd.init(0x27, 1)
lcd.clear()
reader = SimpleMFRC522()
bz = Buzzer(22)
alarm = 0
    
if __name__ == '__main__':
    try:
        while(True):
            mot.wait_for_motion() #wait for motion to be detected
            lcd.clear()
            print("Motion detected!")
            lcd.write(0,0, "Motion Detected!")
            motion = True
            while alarm != 5:
                red0.on()
                bz.on()
                time.sleep(1)
                bz.off()
                red0.off()
                red1.on()
                bz.on()
                time.sleep(1)
                bz.off()
                red1.off()
                alarm = alarm + 1
            alarm = 0
                
            mot.wait_for_no_motion() #wait for no motion to be detected
            lcd.clear()
            print("No motion")
            motion = False
            lcd.write(0,0, "No Motion")
            try:
                while motion == False:
          
    # When 'Ctrl+C' is pressed, the program
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy() 
