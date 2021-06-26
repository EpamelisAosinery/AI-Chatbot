import pyttsx3
import speech_recognition
from datetime import date, datetime

engine_get_audio = speech_recognition.Recognizer()
engine_speaks = pyttsx3.init()
engine_brain = ""

while True:
          #Convert speech into string type for engine_brain to process
          with speech_recognition.Microphone() as mic:
                    print("Robot: I'm listening")
                    audio = engine_get_audio.listen(mic)
          print("Robot: ...")
          try:
                    user = engine_get_audio.recognize_google(audio)
          except:
                    user = ""

          print("User: ", user)

          #Processing the Inputs
          #def engine_brain():
          if user in "":
                    engine_brain = "I can not hear you. Please try again."
          elif "hello" in user:
                    engine_brain = "Hello, how are you?"
          elif "fine"  in user:
                    engine_brain = "That's good to hear. What can I help you today?"
          elif "time"  in user:
                    now = datetime.now()
                    engine_brain = now.strftime("%H hour %M minutes %S seconds")
          elif "today"  in user:
                    today = date.today()
                    engine_brain = today.strftime("%B%d,%Y")
          elif "bye"  in user:
                    engine_brain = "Bye and have a good day."
                    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine_speaks.setProperty('voice', voice_id) 
                    engine_speaks.say(engine_brain)
                    engine_speaks.runAndWait()
                    break
          else:
                    engine_brain = "Sorry, I cannot hear clearly. Please say it slowly. Thank you."

          print("Robot: ", engine_brain)

          voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
          engine_speaks.setProperty('voice', voice_id) 
          engine_speaks.say(engine_brain)
          engine_speaks.runAndWait()