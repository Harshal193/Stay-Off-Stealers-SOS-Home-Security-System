import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import os, time
import serial
import MFRC522
import spi
import signal
import picamera
#GPIO.cleanup()
#camera=picamera.PiCamera()
counter1 = 0;
counter2 = 0;
GPIO.setwarnings(False)
continue_reading = True
GPIO.setup(32,GPIO.OUT)  #SOLENOID trigger pin
GPIO.setup(3,GPIO.IN)  #cont brk1 IN1
GPIO.setup(5,GPIO.IN)  #cont brk2 IN2
GPIO.setup(10,GPIO.IN)  #blynk pin BLYNK
GPIO.setup(11,GPIO.OUT)  #ip1
GPIO.setup(12,GPIO.OUT)  #ip2
GPIO.setup(13,GPIO.OUT)  #for rotating motor reverse
GPIO.setup(31,GPIO.OUT)  #for buzzer
#GPIO.output(32,1)
#time.sleep(5)
#GPIO.output(11,0)
#GPIO.output(12,0)
GPIO.setmode(GPIO.BOARD)
if GPIO.input(3)==0:
    time.sleep(2)
    GPIO.output(32,0)#for solenoid lock
    time.sleep(1)
    GPIO.output(31,1)
    time.sleep(4)
print("door locked")
with picamera.PiCamera() as camera:
	for i in range(2):
		camera.capture('/home/pi/Evidence/picture%s.jpg' % i)
		print("image captured")
with picamera.PiCamera() as camera:
	camera.start_recording("/home/pi/Evidence/footagetest.h264")  #start recording using pi camera
	camera.wait_recording(10)#wait for video to record
	camera.stop_recording()#stop recording
	print("video recording stopped")
#for main gate (loader)
GPIO.output(11,1)
GPIO.output(12,0)#anti clockwise
time.sleep(5)
print("main gate closed")
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)
port.write('ATE0'+'\r\n')      # Disable the Echo
rcv = port.read(10)
print rcv
time.sleep(1)
port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
rcv = port.read(10)
print rcv
time.sleep(1)
port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
rcv = port.read(10)
print rcv
time.sleep(1)
# Sending a message to a particular Number
port.write('AT+CMGS="9404994939"'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)
port.write('Alert! Something is happening wrong outside your house.Open this link to watch it- https://cobaltic-neanderthal-5684.dataplicity.io/stream_simple.html'+'\r\n')  # Message
rcv = port.read(10)
print rcv
port.write("\x1A") # Enable to send SMS
for i in range(10):
	rcv = port.read(10)
	print rcv
print "message sent"    
time.sleep(5)
# Makinng a call to a particular Number
port.write('ATD9404994939;'+'\r\n')
for i in range(10):
	rcv = port.read(20)
	print rcv
time.sleep(2)
print "call connected"
#if GPIO.input(13)==1:
GPIO.output(11,0)
GPIO.output(12,1)#move loader clockwise 
time.sleep(2)  
print "reached at the end of program"
GPIO.cleanup()
