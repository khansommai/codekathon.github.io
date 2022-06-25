import BlynkLib
import socket
import RPi.GPIO as GPIO

#set GPIO pinout
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO 17 for led
gpiopin = 17
#==========
#กำหนดตัวแปร servoPIN ให้มีค่าเท่ากับ GPIO พินที่เชื่อมต่อกับ Servo motor
servoPIN = 21
#กำหนดโหมดของพิน servoPIN เป็นแบบส่งค่าออก
GPIO.setup(servoPIN, GPIO.OUT)
#กำหนดให้พิน servoPIN เป็น PWM ทำงานด้วยความถี่ 50Hz ซึ่งจะสามารถสั่งให้มอเตอร์หมุนช้ากว่าปกติได้
p = GPIO.PWM(servoPIN, 50) 
#สั่งให้เริ่มทำงาน
p.start(7.5)
#========== 

#cloud server
BLYNK_TEMPLATE_ID = ''
BLYNK_DEVICE_NAME = ''
BLYNK_AUTH = ''

blynk = BlynkLib.Blynk(BLYNK_AUTH)

#for data stream Virtual Pin V0
@blynk.on('V0')
def S1_write_handler(value):
  print("value v0 = {}".format(value[0]))  
  if int(value[0]) == 1:
    print('LED on')
    GPIO.setup(gpiopin, GPIO.OUT)
    GPIO.output(gpiopin, GPIO.HIGH)

    #=======
    p.ChangeDutyCycle(12.5) 

  else :
    print('LED off')
    GPIO.setup(gpiopin, GPIO.OUT)
    GPIO.output(gpiopin, GPIO.LOW)  
    #=======
    p.ChangeDutyCycle(7.5) 

@blynk.on("connected")
def blynk_connected():
  print('Updating values from the server...')
  #sync virtual pin V0
  blynk.sync_virtual(0)

if __name__ == "__main__":
    while True:
      try:
        blynk.run()
      except socket.error as e:
        print(e)
        
        blynk.connect()
    #ปิดการทำงาน
    p.stop()
    GPIO.cleanup()
