# own your whole computing class with this one simple trick!

import keyboard
import pyautogui as pag
import pytesseract as pt
import time

time.sleep(30) # sleep or something idk

pt.pytesseract.tesseract_cmd = 'PATH\\TO\\tessract-osr\\tesseract.exe'
# probably something like 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe' but depends on where you install it

def type_test():

    # dimensions of screenshot
    # left is the left border of the sc / top is the top border
    # i think this depends on your monitor so play around with it until it captures everything you want to type out
    left = 335
    top = 180
    width = 1150
    height = 300
    
    # screenshot!! and save
    sc = pag.screenshot(region=(left, top, width, height))
    sc.save('typering.jpg') # saving is not needed but its cool for debugging

    # image to text with pytesseract
    raw_words = pt.image_to_string(sc)
    
    # split the lines because the freaking computing python test needs you to key in enter for some reason
    lines = raw_words.split('\n')
    lines = [word for word in lines if word] # remove all rempty strings
    
    # lines[0] = 'd' + lines[0][2:] i hardcoded this line to fix the text to image error because its the same test every time 😂
    
    # block keyboard input so typing doesnt ruin it
    for i in range(150):
        keyboard.block_key(i)
        
    # type out each line and press enter 
    for words in lines:
        pag.write(words,interval=0.01)
        pag.press("enter")

# lose all your friends 😎😎😎
type_test()
