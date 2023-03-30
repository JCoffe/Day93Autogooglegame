from PIL import Image, ImageDraw
import math
import pyautogui
import webbrowser
import time

url = "chrome://dino/"
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

shape = [(400, 250), (450, 300)]


secs_between_keys = 0.2

webbrowser.get(chrome_path).open(url)

time.sleep(2)

pyautogui.typewrite('chrome://dino/', interval=secs_between_keys)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('space')
time.sleep(2)

def is_object(image):
    data = image.getdata()

    for item in data:
        if item[0] != 255:
            return True
    return False
    
for i in range(0, 300):

    im = pyautogui.screenshot(region=(100,400, 800, 600))
    im_rectangle = ImageDraw.Draw(im)
    im_rectangle.rectangle(shape, outline="red", width=5)
    im2 = pyautogui.screenshot(region=(400,600, 250, 80))



    found_object = is_object(im2)
    print(found_object)
    if found_object:
        pyautogui.press('space')

    time.sleep(0.02)


im2.save("rectangle.jpg")

im.show()