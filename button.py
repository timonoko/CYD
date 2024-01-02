
import time,urequests
from ili9341 import Display, color565
from xpt2046 import Touch
from machine import idle, Pin, SPI
from noko_font import text

RED = color565(255, 0,0)
GREEN = color565(0, 255, 0)
BLUE = color565(0, 0, 255)
CYAN = color565(0, 255, 255)
YELLOW = color565(255, 255, 0)
PURPLE = color565(255, 0, 255)
WHITE = color565(255, 255, 255)
BLACK = color565(0,0,0)

spi1 = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))
display = Display(spi1, dc=Pin(2), cs=Pin(15), rst=Pin(0))
bl_pin = Pin(21, Pin.OUT)
bl_pin.on()

BUTTONS = []

def button(act,txt,x,y,w,h,cf,cb,font='r30'):
    global BUTTONS
    BUTTONS += [[x,y,x+w,y+h,act]]
    display.fill_hrect(x,y,w,h,cb)
    text(x+5,y+10,txt,cf,font,display)

def press(x, y):
    global BUTTONS
    y=320-y
    i = 0
    while i < len(BUTTONS):
        b=BUTTONS[i]
        if x>b[0] and y>b[1] and x<b[2] and y<b[3]:
            act=b[4]
            act(x,y)
            break
        i+=1

spi2 = SPI(2, baudrate=1000000, sck=Pin(25), mosi=Pin(32), miso=Pin(39))
touch = Touch(spi2,cs=Pin(33),int_pin=Pin(36),int_handler=press)


def urequ(x):
    print(x)
    try: urequests.get(x)
    except: 
        print('EI ONNISTU')
        time.sleep(2)
#        try: urequests.get(x)
#        except: print('EI ONNISTU2')


def rON(x):
    urequ('http://192.168.1.65/r%son'%x)

def rOFF(x):
    urequ('http://192.168.1.65/r%soff'%x)

    
def r1ON(x,y): rON(1)
button(r1ON,"ON 1",30,20,70,40,BLACK,GREEN)
def r1OFF(x,y): rOFF(1)
button(r1OFF,"OFF 1",130,20,70,40,WHITE,RED)

def r2ON(x,y): rON(2)
button(r2ON,"ON 2",30,80,70,40,BLACK,GREEN)
def r2OFF(x,y): rOFF(2)
button(r2OFF,"OFF 2",130,80,70,40,WHITE,RED)

def r3ON(x,y): rON(3)
button(r3ON,"ON 3",30,140,70,40,BLACK,GREEN)
def r3OFF(x,y): rOFF(3)
button(r3OFF,"OFF 3",130,140,70,40,WHITE,RED)

def r4ON(x,y): rON(4)
button(r4ON,"ON 4",30,200,70,40,BLACK,GREEN)
def r4OFF(x,y): rOFF(4)
button(r4OFF,"OFF 4",130,200,70,40,WHITE,RED)

def jON(x,y):
    urequ('http://192.168.1.64/5/on')
button(jON,"JUOTIN",30,260,70,40,BLACK,YELLOW,'r20')

def jOFF(x,y):
    urequ('http://192.168.1.64/5/off')
button(jOFF,"JUOTIN",130,260,70,40,WHITE,RED,'r20')

while True:
    pass
