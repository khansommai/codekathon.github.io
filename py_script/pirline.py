import requests
import RPi.GPIO as GPIO
import time
import datetime

# LINE notify
url = 'https://notify-api.line.me/api/notify'
token = 'ใส่รหัส totken ของ line'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#ตัวแปรเก็บตำแหน่งพินที่เชื่อมต่อกับ PIR motion sensor
pir_sensor_pin = 23
#ตัวแปรเก็บตำแหน่งพินที่เชื่อมต่อกับ LED
led_pin = 2
#กำหนดให้รับสัญญาณข้อมูลจาก PIR motion sensor ที่ตำแหน่งพินที่กำหนดในตัวแปร pir_sensor_pin
GPIO.setup(pir_sensor_pin, GPIO.IN)
#กำหนดให้จ่ายกระแสไฟฟ้าออกไปที่ตำแหน่งพินที่กำหนดในตัวแปร led_pin
GPIO.setup(led_pin, GPIO.OUT)           

print("เริ่มต้นทำงาน PIR motion sensor...")

while(True):
        #ถ้ามีสัญญาณเข้ามาจาก PIR motion sensor
        if(GPIO.input(pir_sensor_pin)):
                for i in range(0,2):
                        GPIO.output(led_pin, True)
                        time.sleep(1)
                        GPIO.output(led_pin, False)
                        time.sleep(0.5)

                #สร้างข้อความวันที่
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                msg = 'พบความเคลื่อนไหว: ' + dt
                #สร้างการแจ้งเตือนไปที่ไลน์
                r = requests.post(url, headers=headers, data = {'message':msg})
                print(r.text)
                #แสดงข้อความที่หน้าจอ
                print(msg)
                time.sleep(3)
        time.sleep(1) #loop delay

GPIO.cleanup()
