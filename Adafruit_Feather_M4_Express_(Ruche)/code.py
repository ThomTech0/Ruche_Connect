# Write your code here :-)
import time
import board
import adafruit_bme680
from adafruit_bme280 import basic as adafruit_bme280
import analogio
import digitalio
import pwmio
import math
from adafruit_motor import servo

pin_ouverture = digitalio.DigitalInOut(board.D10)
pin_masse = analogio.AnalogIn(board.A3)
# create a PWMOut object on Pin A1
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm, min_pulse = 500, max_pulse = 2500)
etat_open=88
etat_close=180
suivi=0

my_servo.angle=etat_open

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

temperature_offset_1 = 0.4
temperature_offset_2 = 1

A = 1
B = 0

k=0

while True:


    nombre_mesure = 128
    val = 0
    masse = 0

    for i in range (nombre_mesure):
        a = pin_masse.value
        val = val + a
        
    CAN = val/nombre_mesure
    masse_g = A * CAN + B

    
    temp_int = round(bme680.temperature + temperature_offset_1 , 2)
    temp_ext = round(bme280.temperature + temperature_offset_2 , 2)
    hum_int = round(bme680.relative_humidity , 2)
    hum_ext = round(bme280.relative_humidity , 2)
    masse = round( masse , 1)
    
    print(masse_g)

    print("Temp_int: %0.2f C" % temp_int)
    print("Temp_ext: %0.2f C" % temp_ext)
    print("Hum_int: %0.2f " % hum_int)
    print("Hum_ext: %0.2f \n" % hum_ext)

    ft=open("fichier_transfert.txt", "w")
    ft.write(str(nom)+"/"+str(tag1)+"/"+str(tag2)+"/"+str(tag3)+"/"+str(temp_int) + '/' + str(temp_ext) + '/' + str(hum_int) + '/' + str(hum_ext) + '/' + str(masse) + '/'+str(info_reine)+"/"+str(etat_chant)+"/"+str(k))
    ft.write(str(i))
    ft.close()

    etat = pin_ouverture.value

    if(etat== False  and suivi!=1):
        for angle in range(etat_open, etat_close, 1):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.02)
        suivi=1
        print("Dispositif de sécurité activé")


    if(etat== True and suivi!=0):
        for angle in range(etat_close, etat_open, -1): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.02)
        suivi=0
        print("Dispositif de sécurité désactivé")

    print(suivi)

    time.sleep(1)
