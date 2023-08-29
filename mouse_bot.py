import pyautogui as pag
import random
import time

while True:
    #create random coordinate on computer screen
    x = random.randint(600,700)
    y = random.randint(200,600)

    #the speed the mouse will move to the coordinate
    pag.moveTo(x,y,0.5)

    #move every 2 seconds
    time.sleep(2)