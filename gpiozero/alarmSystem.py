from SimpleMFRC522 import SimpleMFRC522
from gpiozero import MotionSensor
from termcolor import colored
from gpiozero import Buzzer
from gpiozero import LED
import LCD as lcd
import colorama
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
            mot.wait_for_motion()
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
                
            mot.wait_for_no_motion()
            lcd.clear()
            print("No motion")
            motion = False
            lcd.write(0,0, "No Motion")
            print("Hold a tag near the reader to disarm")
            id, text = reader.read()
            if id == [PLACEHOLDER] and text == "Charles Dudley":
                print("ID: %s\nText: %s" % (id,text))
                green0.on()
                bz.on()
                time.sleep(1)
                bz.off()
                time.sleep(9)
                green0.off()
            
            else:
                print(colored("ALERT: BREAK IN!", 'red', attrs=["Underline"]))
          
    except KeyboardInterrupt:
        GPIO.cleanup()
        destroy() 
