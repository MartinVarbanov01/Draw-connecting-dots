from pynput.mouse import Listener
import winsound
import pyautogui

first_click = True
firstX = 0
firstY = 0
listOf = []
with open('draw.txt', 'w') as a:
    a.write("")
a.close()


def on_click(x, y, button, pressed):
    global first_click, firstX, firstY, listOf
    if pressed and str(button) == "Button.left":
        if first_click:
            winsound.Beep(7500, 50)
            first_click = False
            firstX, firstY = x, y
        else:
            winsound.Beep(7500, 50)
            with open('draw.txt', 'a') as f:
                f.write("d," + str(round((x - firstX), 2)) + "," + str(round((firstY - y), 2)) + "\n")
            f.close()
    elif pressed and str(button) == "Button.right":
        with open('draw.txt', 'r') as r:
            listOf = r.readlines()
        r.close()
        try:
            listOf.pop()
            peek = listOf.pop().split(',')
            pyautogui.moveTo(firstX + float(peek[1]), firstY - (float(peek[2])))
            joined = peek[0] + ',' + peek[1] + ',' + peek[2]
            listOf.append(joined)
            temp = ""
            for items in listOf:
                temp += items
            with open('draw.txt', 'w') as w:
                w.write(temp)
            w.close()
        except:
            with open('draw.txt', 'w') as w:
                w.write("")
            w.close()
            pyautogui.moveTo(firstX, firstY)
    elif pressed and str(button) == "Button.middle":
        winsound.Beep(5000, 100)
        with open('draw.txt', 'a') as f:
            f.write("p," + str(round((x - firstX), 2)) + "," + str(round((firstY - y), 2)) + "\n")
        f.close()


with Listener(on_click=on_click) as listener:
    listener.join()
