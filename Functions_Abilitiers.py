#Speaking 
import pyttsx3

engine_speaks = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine_speaks.setProperty('voice', voice_id) 
engine_speaks.say('hi')
engine_speaks.runAndWait()

#Processing the Inputs
def engine_brain():
          if user in "":
                    engine_brain = "I can not hear you. Please try again."
          elif "hello" in user:
                    engine_brain = "Hello, how are you?"
          elif "fine" or "good" in user:
                    engine_brain = "That's good to hear. What can I help you today?"
          elif "time" or "what time is it" or "what is the time" in user:
                    now = datetime.now()
                    engine_brain = now.strftime("%H hour %M minutes %S seconds")
          elif "today" or "what is today" or "what's today" in user:
                    today = date.today()
                    engine_brain = today.strftime("%B%d,%Y")

          else:
                    engine_brain = "Sorry, I cannot hear clearly. Please say it slowly. Thank you."

print("Robot: ", engine_brain)
#Convert speech into string type for engine_brain to process
import speech_recognition

engine_get_audio = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
          print("Robot: I'm listening")
          audio = engine_get_audio.listen(mic)
try:
          user = engine_get_audio.recognize_google(audio)
except:
          user = ""

print("User: ", user)