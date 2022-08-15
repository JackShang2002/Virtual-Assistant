#Imports
from ast import parse
from selenium import webdriver
from tkinter import *
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import re
import pandas as pd
import requests
import speech_recognition as sr
import pyttsx3
import sys
import pywhatkit
import datetime
import wikipedia


#URLs for major news websites
# CBC news: https://www.cbc.ca/news
# Vancouver daily hive: https://dailyhive.com/vancouver
# Wall street journal economy: https://www.wsj.com/news/economy?mod=nav_top_section
# Wall stree journal tech: https://www.wsj.com/news/technology?mod=nav_top_section

listener = sr.Recognizer()
izzy = pyttsx3.init()
voices = izzy.getProperty("voices")
izzy.setProperty("voice", voices[1].id) 

#Says good morning
def GoodMorning():
    print("Good morning.\n")



#Gets top news
def GetTopNews():
    URL = "https://www.cbc.ca/news"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")
    
    #putting all links in a list
    listofLinks = []
    for link in links:
        if(link.has_attr("href")):
            listofLinks.append(link["href"])

    #filter using substring
    linksNews = []
    req1 = "/news/world"
    req2 = "/news/canada"
    req3 = "/news/local"
    for i in listofLinks:
        if(req1 in i):
            linksNews.append("https://www.cbc.ca" + i)
        if(req2 in i):
            linksNews.append("https://www.cbc.ca" + i)
        if(req3 in i):
            linksNews.append("https://www.cbc.ca" + i)
    
    
    #extracting headline and further info
    headline = []
    headLineFiltered = []
    headLineParsed = []
    headLineComplete = []
    desc = []
    for link in linksNews:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        heading = soup.find_all(class_="detailHeadline")
        headline.append(heading)
        descriptions = soup.find_all("p")
        counter = 0
        sd = ""
        for i in descriptions:
            line = descriptions[counter].get_text()
            counter += 1
            sd += line
            desc.append(sd)
    
    
    
    #delete all entries with []
    for i in headline:
        if len(i) > 0:
            headLineFiltered.append(i)


    #parse out everything but the headline and add to headLineParsed
    for item in headLineFiltered:
        newStr = str(item)
        parsedStr = re.split("<|>", newStr)
        headLineParsed.append(parsedStr[2])

    #get rid of duplicates if there are any
    [headLineComplete.append(i) for i in headLineParsed if i not in headLineComplete]

    #print each item to terminal
    for i in headLineComplete:
        print(i)
        #print(desc)

    print("Done!")

    return headLineComplete, desc

#Search up a person
def SearchPerson(target):
    return

#Says some text
def Say(text):
    izzy.say(text)
    izzy.runAndWait()


#Prompts the user for input
def Prompt():
    #AlarmVal = input("Do you want your morning news? Y/N \n")
    #if AlarmVal == "Y" or "y":
        #GoodMorning()
        #headlines, descriptions = GetTopNews()
        #GetHTML()
    
    Say("Izzy here! What do you need?")

    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            request = listener.recognize_google(voice)
            request = request.lower()
            print(request)
    except:
        pass

    return request


#Main function declaration
def main():
    # create a tkinter window
    #root = Tk()             
    #root.geometry('900x600')
    
    # Create a Button
    #closeButton = Button(root, text = 'CLOSE!', bd = '5',
                            #command = root.destroy)

    #promptButton = Button(root, text = 'OPEN!', bd = '5',
                            #command = Prompt)
    
    # Set the position of button on the top of window.  
    #closeButton.pack(side = 'top')
    #promptButton.pack(side = 'bottom')   
    
    #root.mainloop()
    while True:
        request = Prompt()
        if "get the morning news" in request:
            headlines = []
            descriptions = []
            headlines, descriptions = GetTopNews()
            for h in headlines:
                Say(h)
        
        elif "repeat please" in request:
            request = Prompt()
        
        elif "play" in request:
            song = request.replace("play", "")
            Say("playing" + song + "now")
            pywhatkit.playonyt(song)
        
        elif "get me notes on" in request:
            inquiry = request.replace("get me notes on", "")
            notes = wikipedia.summary(inquiry, 1)
            print(notes)
            Say(notes)

        elif "get me this guy's info" in request:
            target = request.replace("get me this guy's info", "")
            SearchPerson(target)

        elif "that will be all for now" in request:
            Say("okay, have a great day!")
            sys.exit()

    
        
        
 

#Execute program
if __name__ == "__main__":
    main()