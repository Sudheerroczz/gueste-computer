import serial 
import time 
import pyautogui
ArduinoSerial = serial.Serial('com3',9600)
time.sleep(2)
while 1:
    incoming = str (ArduinoSerial.readline())
    print (incoming)
    

    if 'enter' in incoming:
        pyautogui.typewrite(['enter'], 0.2)

    if 'left' in incoming:
        pyautogui.hotkey('left')  

    if 'right' in incoming:
        pyautogui.hotkey('right') 
 
    if 'up' in incoming:
        pyautogui.hotkey('up')
        
    if 'down' in incoming:
        pyautogui.hotkey('down')
    
    if 'exit' in incoming:
        pyautogui.hotkey('alt', 'f4')

    if 'start' in incoming:
        pyautogui.typewrite(['win'], 0.2)

    incoming = "";
    
 
