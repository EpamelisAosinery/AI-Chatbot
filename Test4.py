

import pyttsx3
from datetime import date, datetime
import re

ruby_speak = pyttsx3.init()

def begin():
          you = input(
                    "Ruby:\n\tWhat can I help you? "\
                    "\nYou: \t")

          if "hello" in you:

                    process =("Hi, how are you?")
                    print("Ruby:\n\Hi, how are you?")
                    
                    return process

# MAIN

proocess = begin()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
ruby_speak.setProperty('voice', voice_id) 
ruby_speak.say(proocess)
ruby_speak.runAndWait()

#Terminal.app