from time import sleep
import sys
from SimpleMFRC522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(2)
        text=input("What would you like to write?")
        print("Hold a tag near the reader to write")
        reader.write(text)
        print("Written!")
        sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
