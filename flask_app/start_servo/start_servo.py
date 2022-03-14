from gpiozero import Servo
from time import sleep
import random
 
def startServo(mode):
    if mode == 'beginner':
        myGPIO=17
        myCorrection=0
        maxPW=(2.0+myCorrection)/1000
        minPW=(1.0-myCorrection)/1000
        servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
        #turn on the servo
        while True:
            servo_num = round(random.uniform(-.6, .6),1)
            sleep_num = random.randrange(4)
            print('Servo value: ' + str(servo_num))
            print('Sleeping for: ' + str(sleep_num) + ' Seconds...')
            servo.value = servo_num
            sleep(sleep_num)
    elif mode == 'intermediate':
        myGPIO=17
        myCorrection=0
        maxPW=(2.0+myCorrection)/1000
        minPW=(1.0-myCorrection)/1000
        servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
        #turn on the servo
        while True:
            servo_num = round(random.uniform(-1, 1),1)
            sleep_num = random.randrange(3)
            print('Servo value: ' + str(servo_num))
            print('Sleeping for: ' + str(sleep_num) + ' Seconds...')
            servo.value = servo_num
            sleep(sleep_num)
    elif mode == 'advanced':
        myGPIO=17
        myCorrection=0
        maxPW=(2.0+myCorrection)/1000
        minPW=(1.0-myCorrection)/1000
        servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
        #turn on the servo
        while True:
            servo_num = round(random.uniform(-1, 1),1)
            sleep_num = random.randrange(2)
            print('Servo value: ' + str(servo_num))
            print('Sleeping for: ' + str(sleep_num) + ' Seconds...')
            servo.value = servo_num
            sleep(sleep_num)

if __name__ == '__main__':
    startServo(mode)

