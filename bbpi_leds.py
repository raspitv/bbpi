from gpiozero import LED
from time import sleep
red = LED(4)
white = LED(10)
green = LED(16)
blue = LED(21)
yellow = LED(27)
leds = [red, white, green, blue, yellow]
while True:
  for led in leds:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
  
