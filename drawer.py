import time
import pyautogui
from pynput.mouse import Listener

size = int(input("Enter size: "))
first_click = True
firstX = 0
firstY = 0
xList = []
yList = []
tList = []
draw_once = True
with open('draw.txt', 'r') as r:
    listOf = r.readlines()
    listOf.pop()
r.close()
for cord in listOf:
    split = cord.split(",")
    tList.append(split[0])
    xList.append(int(split[1]))
    yList.append(int(split[2]))


def draw_now():
    for i in range(len(xList)):
        draw(tList[i], xList[i], yList[i])


def draw(t, a, b):
    a = a / size
    b = b / size
    a = a + firstX
    b = firstY - b
    if 1920 - a > 0 and 1080 - b > 0:
        if t == 'd':
            pyautogui.moveTo(x=a, y=b, duration=0.0)
        if t == 'p':
            pyautogui.mouseUp(button='left')
            pyautogui.moveTo(x=a, y=b, duration=0.0)
            pyautogui.mouseDown(button='left')


def on_click(x, y, button, pressed):
    global firstX, firstY, draw_once
    if pressed and draw_once:
        draw_once = False
        firstX = x
        firstY = y
        time.sleep(0.5)
        pyautogui.mouseDown(button='left')
        time.sleep(0.5)
        draw_now()
        pyautogui.mouseUp(button='left')
        exit()


with Listener(on_click=on_click) as listener:
    listener.join()
