import time
from RPi import GPIO
from RPi._GPIO import BCM
import lcd

sensor = 4

GPIO.setmode(BCM)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lcd.lcd_init()


def meterPerSecondeKenneth():
    omwenteligen = 0
    vorigeWaarde = 1

    tijd1 = time.time()
    tijd2 = time.time()



    while (tijd2 - tijd1) <= 1:

        sensorwaarde = GPIO.input(4)

        if vorigeWaarde != sensorwaarde:
            omwenteligen += 1
            vorigeWaarde = sensorwaarde

        else:
            vorigeWaarde = sensorwaarde

        tijd2 = time.time()

      #omtrek wiel 21,6769 cm


    return ((omwenteligen/2)*0.2167)*3.6

try:

    while True:
        tekst = round(meterPerSecondeKenneth(),2)
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_byte(0x01, False)
        time.sleep(0.03)
        lcd.lcd_string(str(tekst),2)




        # lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        # lcd.lcd_string(lcd.get_ip_son(), 2)

        # print("--------------------------------------------")


        # time.sleep(0.1)
        # print(duration)
except KeyboardInterrupt:
    GPIO.cleanup()


