import RPi.GPIO as GPIO
import time

Trig_Pin = 20
Echo_Pin = 21
Led_Pin = 16
maximum_dis = 80

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Led_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)

time.sleep(2)

def checkdist():
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2-t1)*340*100/2


try:
    while True:
        if(checkdist() > maximum_dis)
           {
               print 'warning'
               GPIO.output(Led_Pin, GPIO.HIGH)
           }
        else
           print 'Distance:%0.2f cm' % checkdist()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
