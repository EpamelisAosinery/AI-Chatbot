import pyttsx3

ruby_speak = pyttsx3.init()

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
ruby_speak.setProperty('voice', voice_id) 
ruby_speak.say("hello")
ruby_speak.runAndWait()