import RPi.GPIO as GPIO
import time

def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)
	return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while 1==1:
	blink(11)
GPIO.cleanup()

