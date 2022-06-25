import time
import board
import adafruit_dht
import BlynkLib
from datetime import datetime

#Blynk cloud server
BLYNK_TEMPLATE_ID = 'TMPLJQladeJB'
BLYNK_DEVICE_NAME = 'Weather'
BLYNK_AUTH = 'รหัส Totken ที่ได้จาก Blink.cloud'

# ประกาศตัวแปรสำหรับเริ่มทำงานกับ Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# ประกาศตัวแปรสำหรับเริ่มทำงานกับเซ็นเซอร์ ซึ่่งเชื่อมต่อกับพิน GPIO 4
dhtDevice = adafruit_dht.DHT11(board.D4)

while True:
    #run the Blynk
    blynk.run()
    try:
        # รับค่าอุณหภูมิที่อ่านได้จากเซ็นเซอร์ หน่วยเป็นองศาเซลเซียส
        temperature_c = dhtDevice.temperature
        # แปลงจาก Celcius เป็น Farenheit
        temperature_f = temperature_c * (9 / 5) + 32
        # รับค่าความชื้นที่อ่านได้จากเซ็นเซอร์
        humidity = dhtDevice.humidity
        # พิมพ์ค่า temperature_f, temperature_c และ humidity ออกไปที่หน้าจอ
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        # ส่งค่า temperature_c ไปยัง Blynk cloud server โดยใช้ virtual pin V0
        blynk.virtual_write(0, temperature_c) 
        # ส่งค่า humidity ไปยัง Blynk cloud server โดยใช้ virtual pin V1
        blynk.virtual_write(1, humidity)

        # หาค่าวันที่และเวลาปัจจุบัน
        now = datetime.now()
        # แปลงค่าวันที่ให้เป็นข้อความในรูปแบบ dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # ส่งค่า dt_string ไปยัง Blynk cloud server โดยใช้ virtual pin V2
        blynk.virtual_write(2, dt_string)

    except RuntimeError as error:
        # พิมพ์ข้อความ Error กรณีเกิดความผิดพลาดอ่านค่าจากเซ็นเซอร์ไม่ได้
        print("Error : {}".format(error.args[0]))
        # หน่วงเวลา 2.0 วินาที
        time.sleep(2.0)
        # เริ่มวนลูปใหม่
        continue
    except Exception as error:
        # พิมพ์ข้อความ Error กรณีเกิดความผิดพลาดที่ตัวเซ็นเซอร์
        print("divce error")
        # หยุดการทำงาน
        dhtDevice.exit()
        raise error
    time.sleep(2.0)
