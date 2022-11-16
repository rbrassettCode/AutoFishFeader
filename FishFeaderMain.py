import RPi.GPIO as GPIO
import time
import datetime
import schedule

#### General purpase method to spin motor
def turnMotor() :
    print("Rotate to dispense food.")

    print ("Rotating at intervals of 12 degrees")
    duty = 2
    while duty <= 17:
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1

    print ("Turning back to 0 degrees")
    servo.ChangeDutyCycle(2)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

#### Method that controls dispensing of food for fish
def initMotorOnAndDispense() :
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)

    servo = GPIO.PWM(11,50)

    servo.start(0)
    print ("Waiting for 1 second")
    time.sleep(1)

    turnMotor() #Call turning method to dispense food

    Servo.stop()
    GPIO.cleanup()
    print ("Everything's cleaned up")

#Set scheduler to run at given time
schedule.every().day.at("12:00").do(initMotorOnAndDispense,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) #Wait 1 minutes