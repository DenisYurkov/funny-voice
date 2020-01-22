""" 
funny_voice.py
Create: Denis Yurkov.
"""

# import models.
import pyautogui
import pyttsx3

# init.
engine = pyttsx3.init()

# getting details of current voice.
voices = engine.getProperty('voices')

# changing index, changes voices. 1 for female, on russian use 2.
engine.setProperty('voice', voices[2].id)

start_program = True
while start_program:
    
    # gui.
    gui_message = pyautogui.alert(text='Введите предложение или слова, и послушайте изменения его голоса.', title='Funny Voice')
    gui_prompt = pyautogui.prompt(text='Введите слова или предложение для озвучки: ', title='Funny Voice')

    # logic.
    if gui_prompt:
        engine.say(gui_prompt)
        engine.runAndWait()
        
        gui_exit = pyautogui.confirm(text='Хотите ли вы выйти?', title='Funny Voice')
        if gui_exit == "OK":
            start_program = False
        else:
            start_program = True
            
