# Importing the Necessary Libraries
import speech_recognition as sr
import pyttsx3
import pandas as pd
import os
import pywhatkit
import datetime
import wikipedia
# Importing csv
df=pd.read_csv("O16CSE.csv")
#Filling serial number with empty space
df.set_index([[''] * len(df)], inplace=True)
#Initializing the speech recognizer and text to speech converter
listner = sr.Recognizer()
engine = pyttsx3.init()
#setting voice speed rate
engine.setProperty("rate", 120)
#Using device microphone as a source speech recognizer takes input
run=True
while run:
    with sr.Microphone() as source:
        engine.say('please speak with me now')
        engine.runAndWait()
        print('speak')
        voice = listner.listen(source)
        command = listner.recognize_google(voice)
        command = command.lower()
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        if 'what is your name' in command:
            engine.say('my name is bobb. ')
            engine.runAndWait()
        elif 'bob' in command:
            engine.say('things you spoke to me is..')
            engine.say(command)
            print(command)
            engine.runAndWait()
            if 'who are you' in command:
                engine.say('i am your personalised voice assistant ')
                engine.runAndWait()
            elif 'shut down' in command:
                os.system("shutdown /s /t 1")
            elif 'restart' in command:
                os.system("shutdown /r /t 1")
            elif 'logout' in command:
                os.system("shutdown -l")
            elif 'play' in command:
                command = command.replace('bob play', "")
                engine.say('playing' + command)
                pywhatkit.playonyt(command)
                engine.runAndWait()
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                engine.say(time)
                engine.runAndWait()
            elif 'info' in command:
                command = command.replace('bob give me info about', "")
                info = wikipedia.summary(command, 5)
                print(info)
                engine.say(info)
                engine.runAndWait()
            elif 'student profile' in command:
                command = command.replace('bob give me the student profile ', "")
                command = command.replace('', "")
                command = int(command)
                df1 = df[(df['ID'] == command)]
                print(df1)
                engine.say('student details')
                df2 = df1[['NAME']]
                df3 = df1[['BRANCH']]
                df4 = df1[['ATTENDANCE ']]
                engine.say(df2.to_string())
                engine.say(df3.to_string())
                engine.say(df4.to_string())
                engine.runAndWait()
            elif 'topper' in command:
                a = df['TOTAL']
                topper = a.max()
                df1 = df[(df['TOTAL'] == topper)]
                print(df1[['ID', 'NAME', 'TOTAL']])
                engine.say('ID', 'student details')
                df2 = df1[['NAME', 'TOTAL']]
                engine.say(df2.to_string())
                engine.runAndWait()
            elif 'least attendance' in command:
                a = df['ATTENDANCE ']
                L_A = a.min()
                df1 = df[(df['ATTENDANCE '] == L_A)]
                print(df1[['ID', 'NAME', 'BRANCH', 'ATTENDANCE ']])
                df2 = df1[['ID', 'NAME', 'BRANCH', 'ATTENDANCE ']]
                engine.say(df2)
                engine.runAndWait()
            elif 'subject' in command:
                if 'least' in command:
                    if 'software engineering' in command:
                        a = df['SE']
                        ff = a.min()
                        df1 = df[(df['SE'] == ff)]
                        print(df1[['ID', 'NAME', 'SE']])
                        df2 = df1[['ID', 'NAME', 'SE']]
                        engine.say(df2)
                        engine.runAndWait()
                    elif 'computer netwroks' in command:
                        a = df['CN']
                        ff = a.min()
                        df1 = df[(df['CN'] == ff)]
                        print(df1[['ID', 'NAME', 'CN']])
                        df2 = df1[['ID', 'NAME', 'CN']]
                        engine.say(df2)
                        engine.runAndWait()
                    elif 'database management system' in command:
                        a = df['DBMS']
                        ff = a.min()
                        df1 = df[(df['DBMS'] == ff)]
                        print(df1[['ID', 'NAME', 'DBMS']])
                        df2 = df1[['ID', 'NAME', 'DBMS']]
                        engine.say(df2)
                        engine.runAndWait()
                elif 'top' in command:
                    if 'software engineering' in command:
                        a = df['SE']
                        ff = a.max()
                        df1 = df[(df['SE'] == ff)]
                        print(df1[['ID', 'NAME', 'SE']])
                        df2 = df1[['ID', 'NAME', 'SE']]
                        engine.say(df2)
                        engine.runAndWait()
                    elif 'computer netwroks' in command:
                        a = df['CN']
                        ff = a.max()
                        df1 = df[(df['CN'] == ff)]
                        print(df1[['ID', 'NAME', 'CN']])
                        df2 = df1[['ID', 'NAME', 'CN']]
                        engine.say(df2)
                        engine.runAndWait()
                    elif 'database management system' in command:
                        a = df['DBMS']
                        ff = a.max()
                        df1 = df[(df['DBMS'] == ff)]
                        print(df1[['ID', 'NAME', 'CN']])
                        df2 = df1[['ID', 'NAME', 'CN']]
                        engine.say(df2)
                        engine.runAndWait()
    if command == ''or command=='bob exit':
            run = False
engine.say('thank you')
engine.runAndWait()
