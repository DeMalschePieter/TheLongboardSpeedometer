import time
from RPi import GPIO
from RPi._GPIO import BCM
import lcd

sensor = 4

GPIO.setmode(BCM)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lcd.lcd_init()


# vorigeWaarde = 1
# aantalkeer = 0
# aantalMeter = 0
#
#
# start = default_timer()
# secondtimer = default_timer()

# def perseconde():
#     aantalMeter2 = 0
#     sensoor = GPIO.input(sensor)
#     secondentijd = default_timer() - start
#
#     while secondentijd <= 1:
#         secondentijd = default_timer() - start
#         if sensoor != vorigeWaarde:
#             aantalMeter2 += 0.1
#
#         voorigewaarde = sensoor
#     return aantalMeter2 * 3.6
#
#
# def meterPerSeconde():
#     vorigeWaarde = 1
#     aantalkeer = 0
#     aantalMeter = 0
#     sensorwaarde = GPIO.input(12)
#
#
#     tijd1 = time.time()
#     tijd2 = time.time()
#     while (tijd2 - tijd1) <= 1:
#         if sensorwaarde != vorigeWaarde:
#             aantalkeer += 0.5
#             aantalMeter += 0.1
#
#
#         vorigeWaarde = sensorwaarde
#         tijd2 = time.time()
#
#     return aantalMeter


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


        # aantalSeconden = default_timer() - start
        # sensorwaarde = GPIO.input(sensor)
        #
        #
        #
        # if sensorwaarde != vorigeWaarde:
        #     aantalkeer += 0.5
        #     aantalMeter += 0.1
        #
        #
        # vorigeWaarde = sensorwaarde



        # Print out results


        # sensoor = GPIO.input(sensor)
        # secondentijd = default_timer() - start
        #
        #
        # while secondentijd <= 1:
        #     secondentijd = default_timer() - start
        #     if sensoor != vorigeWaarde:
        #         aantalMeter2 += 0.1
        #
        #     voorigewaarde = sensoor


        # omwenteligen = 0
        # vorigeWaarde = 1
        #
        # tijd1 = time.time()
        # tijd2 = time.time()
        #
        # while (tijd2 - tijd1) <= 1:
        #
        #     sensorwaarde = GPIO.input(4)
        #
        #     if vorigeWaarde != sensorwaarde:
        #         omwenteligen += 1
        #         vorigeWaarde = sensorwaarde
        #
        #     else:
        #         vorigeWaarde = sensorwaarde
        #
        #     tijd2 = time.time()
        #
        #     # omtrek wiel 21,6769 cm
        #
        # str(round((((omwenteligen / 2) * 0.2167) * 3.6),2))






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

        # Wait before repeating loop
except KeyboardInterrupt:
    GPIO.cleanup()


