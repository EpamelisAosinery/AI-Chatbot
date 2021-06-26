from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from datetime import date, datetime
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
""" # Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "my-new-bucket"

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print("Bucket {} created.".format(bucket.name))

client = language.LanguageServiceClient.from_service_account_json("H:\TRIAL AND ERROR\Python.python\Py apps\gTTSVoiceAssistant-5cedd253dfeb.json")
 """
""" SCOPES = ['https://www.googleapis.com/auth/calendar.readonly'] """


def speak(text):
        tts = gTTS(text=text, lang="en")
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)


def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""

        try:
                said = r.recognize_google(audio)
                print("User: " + said)
        except Exception as e:
                print("Exception: " + str(e))

        return said 

today = date.today()
print (today.strftime("%B %d, %Y"))
now = datetime.now()
print (now.strftime("%H hours %M minutes %S seconds\n"))


text = get_audio()

if "hello" in text:
        speak("hello, how are you?\n")
        print("Ruby: Hello, how are you? ")

if "fine" in text:
        speak("What can I help you today?\n")
        print("Ruby: Hello, how are you? ")

if "what is your name" in text:
        speak("My name is Ruby")
        print("Ruby: Hello, how are you? ")

if "what is today" or "what's today" or "today" in text:
        speak("Today is" + today.strftime("%B %d, %Y"))  
        print("Ruby: Today is " + today.strftime("%B %d, %Y") )
          
""" if "what time is it" or "time" in text:
        speak("It's " + now.strftime("%H hours %M minutes %S seconds"))
        print("Ruby: It is " + now.strftime("%H hours %M minutes %S seconds\n")) """

""" 
def main():
    """       """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
          """ """
        creds = None
        if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                        creds = pickle.load(token)

        if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
        else:
                flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                maxResults=10, singleEvents=True,
                                orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
                print('No upcoming events found.')
        for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])

if __name__ == '__main__':
        main()
 """