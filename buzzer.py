from machine import Pin, PWM
from neopixel import NeoPixel
from utime import sleep

# Definir pines de entrada con resistencias pull-down internas
a = Pin(33, Pin.IN, Pin.PULL_DOWN)
b = Pin(32, Pin.IN, Pin.PULL_DOWN)
c = Pin(35, Pin.IN, Pin.PULL_DOWN)
d = Pin(34, Pin.IN, Pin.PULL_DOWN)

pixels = NeoPixel(Pin(23), 16)

# Definir pines de salida para los LEDs
led1 = [(255, 0, 0)] * 16  # Rojo puro
led2 = [(0, 0, 255)] * 16  # Azul puro

buzzer = PWM(Pin(22))
buzzer.freq(10)

# Frecuencias en Hz para las notas de la imagen
notas = [523, 392, 330, 440, 494, 440, 415, 440, 415, 392]  

# Duraciones ajustadas para que suene más natural
tiempos = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.25, 0.5]

while True:

    A = a.value()
    B = b.value()
    C = c.value()
    D = d.value()

    if (A and C) or (C and D) or (A and B): 
        for i in range(0,8):
            pixels[i] = led1[i]  # Asignar rojo en los primeros 8 LEDs
        pixels.write()
        print (A,B,C,D)

    else:
        for i in range(16):
            pixels[i] = (0, 0, 0)
        pixels.write()

    
    if (not D and not C and B and A) or \
       (not D and C and not B and A) or \
       (not D and C and B and A) or \
       (D and not C and B and A) or \
       (D and C and not B and not A) or \
       (D and C and not B and A) or \
       (D and C and B and not A) or \
       (D and C and B and A):

        for i in range(8,16):
            pixels[i] = led2[i]  # Asignar azul en los últimos 8 LEDs
        pixels.write()
        print (A,B,C,D)

        for i in range(len(notas)):
            buzzer.freq(notas[i])
            sleep(tiempos[i])  # Usa la duración ajustada para cada nota

        buzzer.freq(10)  # Apaga el sonido

    else:
        for i in range(16):
            pixels[i] = (0, 0, 0)
        pixels.write()
