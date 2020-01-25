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

# changing index, changes voices.
# this for Windows use 1 for female, on man use 2.
# this for Linux use 2.
engine.setProperty('voice', voices[1].id)

start_program = True
while start_program:
    
    # gui.
    gui_message = pyautogui.alert(text='Enter a sentence or words, and listen to the changes in his voice.', title='Funny Voice')
    gui_prompt = pyautogui.prompt(text='Enter a word or sentence to voice: ', title='Funny Voice')

    # logic.
    if gui_prompt:
        engine.say(gui_prompt)
        engine.runAndWait()
        
        gui_exit = pyautogui.confirm(text='Do you want to go out?', title='Funny Voice')
        if gui_exit == 'OK':
            start_program = False
        else:
            start_program = True 
    else:
        start_program = False
