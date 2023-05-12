# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:48:01 2023

@author: HP
"""

import openai
openai.api_key="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"
model_engine="gpt-3.5-turbo"
#This specifies which GPT model to use,as there are several models available

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#prinr(voices[1].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runandWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")
        
    else:
        speak("Good Evening!!")
    
    speak("I am your personal Assistant Sir.How can I help you?")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.puse_threshold=1
        audio=r.record(source,duration=4)
        print(audio)
        #audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("User said:{0}\n".format(query))
        
    except Exception:
        #print(e)
        print("Sya that again please...")
        return "None"
    return query

if __name__=="__main___":
    wishMe()
    while True:
        #if 1:
        query=takeCommand().lower()
            
        #Logic for exwcution tasks based query
        if 'chat gpt' in query:
            speak('Welcome to ChatGPT.Press any key when you are ready to speak')
            key=input()
            while True:
                query=''
                query=takeCommand().lower()
                if(query=="search engine exit"):
                    break
                try:
                    #results=wikipedia.summary(query,sentences=2)
                    response=openai.ChatCompletion.create(
                        model='gpt-3.5-turbo',
                        messages=[
                            {"role":"user","content":"{}".format(query)},
                            ])
                    message=response.choice[0]['message']
                    
                except:
                    print('please retry')
                speak("According to my knowledge")
                print(message['content'])
                speak(message['content'])
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
                
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            music_dir=""
            songs=os.listdir(music_dir)
            print(songs)
            os.stratfile(os.path.join(music_dir,songs[0]))
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strtime("%H:%M,%S")
            speak("The time is {}".format(strTime))
         
        elif 'exit' in query:
            break
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    