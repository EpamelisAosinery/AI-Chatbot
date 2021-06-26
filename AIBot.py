
import pyttsx3
import speech_recognition 
from datetime import date, datetime

ruby_listen = speech_recognition.Recognizer()
ruby_speak = pyttsx3.init()
ruby_process = ""

while True:
          # Listen 
          with speech_recognition.Microphone() as mic:
                    print("Ruby is listening...")
                    audio = ruby_listen.listen(mic)

          print("Ruby: ...")

          try:
                    you = ruby_listen.recognize_google(audio)
          except:
                    you == ""

          print("You:" ,  you)

# Understand Processing/ AI Process
def brain_process():
          if you in "":
                    ruby_process = "I can't hear you, try again."
          elif  "today" in you:
                    today = date.today()
                    ruby_process = today.strftime("%B %d, %Y")
          elif "time" in you: 
                    now = datetime.now()
                    ruby_process = now.strftime("%H hours %M minutes %S seconds")
          elif "bye" in you:
                    ruby_process = "Do you want to stop ?"
                    if "yes" in you:
                              ruby_process = "What else can I help you?"
                    elif "no" in you:
                              pass
                    
          else:
                    ruby_process = "I'm fine fine thank you."
          

print("Ruby: ", ruby_process)

# Ruby Speaks
# Use female voice 
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

ruby_speak.setProperty('voice', voice_id) 
ruby_speak.say(ruby_process)
ruby_speak.runAndWait() 

# This is a male voice 
""" ruby.say("Hello Epamelis")
ruby.runAndWait() """

""" voices = ruby.getProperty('voices') 
for voice in voices: 
# to get the info. about various voices in our PC  
print("Voice:") 
print("ID: %s" %voice.id) 
print("Name: %s" %voice.name) 
print("Age: %s" %voice.age) 
print("Gender: %s" %voice.gender) 
print("Languages Known: %s" %voice.languages)  """




