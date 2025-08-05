from SimpleMFRC522 import SimpleMFRC522
from gpiozero import MotionSensor
from gpiozero import Buzzer
from gpiozero import LED
import LCD as lcd
import keyboard
import time
import sys

# ---Hardware Setup---
mot = MotionSensor(17)
red0 = LED(21)
red1 = LED(13)
green0 = LED(5)
blue0 = LED(27)
lcd.init(0x27, 1)
lcd.clear()
reader = SimpleMFRC522()
bz = Buzzer(22)

alarm = 0

# ---Time Setup---
current_timestamp = time.ctime()
    
if __name__ == '__main__':
    try:
        while(True):
                    mot.wait_for_motion()
                    lcd.clear()
                    print(f"{current_timestamp}: Motion detected!")
                    lcd.write(0,0, "Motion Detected!")
                    motion = True
                    while alarm != 1:
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
                    """
                    if id == 45610763277:
                        print("ID: %s\nText: %s" % (id,text))
                        lcd.clear()
                        lcd.write(0,0, "Welcome")
                        lcd.write(0,1, text)
                        blue0.on()
                        bz.on()
                        time.sleep(1)
                        bz.off()
                        time.sleep(9)
                        blue0.off()
                
                    else:
                        print(f"{formatted_datetime}: Suspicious actvity detected. Invalid card used")
                        lcd.clear()
                        lcd.write(0,0, "Invaild card") 
                        lcd.write(0,1, "detected")
                        bz.on()
                        red0.on()
                        red1.on()
                        time.sleep(10)
                        red0.off()
                        red1.off()
                        bz.off()
                    """
      
    except KeyboardInterrupt:
        GPIO.cleanup()
        destroy() 
