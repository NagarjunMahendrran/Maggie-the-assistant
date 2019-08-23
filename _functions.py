import time
from time import time, sleep
import os
import webbrowser 
import speech_recognition as sr
import webbrowser
import pyttsx
import pyautogui
import datetime
import string
from jira import JIRA
from random import *
now = datetime.datetime.now()
                                                                                
def acknowlge(output):
  engine = pyttsx.init()
  engine.setProperty('voice','english+f2')
  engine.setProperty('rate', 190)
  engine.say(output)
  engine.runAndWait()
 
def age():
    age = now.year - 2018
    if(age<1):
       acknowlge('I am still a baby')
    else:
      age = years - 1
      acknowlge('-I am %s old.'%age)

def openoutlook():
  url ="https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office365.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=0&client-request-id=889001fc-b1bd-4122-9c1e-17abfcbd975c&protectedtoken=true&nonce=636666446077733254.4647171e-d100-4870-88ff-d29990428444&state=DYtBDoAwCASpxudgoV2BPsek9urR78skM7cpRLSnW1okQ27dEsDE3XtvF04YXF0fnirCCBeOWItnG2MIWgAo-R71_e76Aw"
  webbrowser.open_new_tab(url)
  acknowlge("Opened Outlook")

def new_tab():
    pyautogui.hotkey('ctrl', 't')

def new_window():
    pyautogui.hotkey('ctrl', 'n') 

def openyoutube():
  url ="https://www.youtube.com"
  webbrowser.open_new_tab(url)
  acknowlge("Opened Youtube")

def open_googlemaps(path):
    url ="https://www.google.com/maps"
    webbrowser.open(url)
    sleep(2)
    common('tab')
    common('tab')
    common('enter')
    sleep(1)
    pyautogui.typewrite(path.split('to')[0])
    common('tab')
    common('tab')
    pyautogui.typewrite(path.split('to')[1])
    common('enter')
    sleep(1)
    acknowlge("Here is your best routes")



def show_my_route():
    r = sr.Recognizer()
    acknowlge("Please let me know the source and  destination")
    with sr.Microphone() as source:
       sleep(1)
       audio = r.listen(source,phrase_time_limit=4)
    try:
       coordinates = r.recognize_google(audio)
       open_googlemaps(coordinates)
    except sr.UnknownValueError:
       acknowlge("I cannot understand the words I am sorry boss")
    except sr.RequestError as e:
       acknowlge("Please change your tone and speak")



def dhanu_main_thread(keyword):
    call_fun_input(keyword)

def common(key_word):
    pyautogui.press(key_word)

def sucide():
    acknowlge("See you soon boss Take care")
    sleep(3)
    pyautogui.hotkey('ctrl', 'z')

def type_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       acknowlge("Say something")
       audio = r.listen(source,phrase_time_limit=5)
    try:
       pyautogui.typewrite(r.recognize_google(audio))
    except sr.UnknownValueError:
       acknowlge("I cannot understand the words I am sorry boss")
    except sr.RequestError as e:
       acknowlge("Please change your tone and speak")

def call_fun_input(keyword):
    # Get the function from switcher 
    func = switcher.get(keyword, "Invalid")
    # Execute the function
    if (func != "Invalid"):
      return func()
    else:
      print("I am not able to understand at this point of time.")

def page_up():
    common("pageup")

def page_down():
    common("pagedown")

def print_screen():
    common("printscreen")

def open_mywipro():
    url = "https://mywipro.wipro.com"
    webbrowser.open_new_tab(url)
    acknowlge("Opened My Wipro")

def open_chrome():    
    url = "http://www.google.com/"
    webbrowser.open_new_tab(url)
    acknowlge('OPENED CHROME')

def close_chrome():
    browserExe = "chrome"
    os.system("pkill "+browserExe)
    acknowlge('CLOSED CHROME')

def clone_custo():
    os.system("gnome-terminal -e 'bash -c \" exec bash\"'")
    common('enter')
    pyautogui.typewrite('cd ~/custo_world/')
    common('enter')
    pyautogui.typewrite('mkdir custo_'+str(now.month)+"_"+str(now.day))
    common('enter')
    pyautogui.typewrite('cd  custo_'+str(now.month)+"_"+str(now.day))
    common('enter')
    pyautogui.typewrite('git clone git@10.142.107.124:/openwrt/custo.git')
    common('enter')

def rebase_custo():
    os.system("gnome-terminal -e 'bash'")
    pyautogui.typewrite('cd ~/custo_world/custo_'+str(now.month)+"_"+str(now.day)+'/custo/')
    common('enter')
    pyautogui.typewrite('git pull --rebase')
    common('enter')

def random_string():
    min_char = 8
    max_char = 12
    allchar = string.ascii_letters + string.digits
    password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    pyautogui.typewrite(password)

def hot_key_type():
    pyautogui.hotkey('ctrl', 'a')

def my_name():
    acknowlge("You are my boss Nagarjun Mahendran")

def maggiee():
    acknowlge("I am Arjun's assistant")

def jira_status_fetch(bugId):
    print("BUGID: "+bugId)
    jira_options={'server': 'https://jira.technicolor.com'}
    jira = JIRA(options=jira_options,basic_auth=('wipro_nagarjunm', 'X6BH9bJgHxLY'))
    sleep(1)
    issue = jira.issue(bugId)
    print("-------------------------------------------------------------------------")
    print("|  Status      :"+issue.fields.status+"                                 |") 
    print("|  Assinee     :"+issue.fields.assignee.displayName+"                   |")
    print("|  Issue Type  :"+issue.fields.issuetype.name+"                         |")
    print("|  Reporter    :"+issue.fields.reporter.displayName+"                   |")
    print("-------------------------------------------------------------------------")
    acknowlge("Please have a look at your Results:")
 

def jira_status():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       acknowlge("Please tell Jira ID")
       sleep(1)
       audio = r.listen(source,phrase_time_limit=3)
    try:
       jira_status_fetch("NG-"+r.recognize_google(audio))
    except sr.UnknownValueError:
       acknowlge("I cannot understand the words I am sorry boss")
    except sr.RequestError as e:
       acknowlge("Please change your tone and speak")    

def min_maxwindow():
    common("f11")

def enter():
    common('enter')

def reminder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       acknowlge("Please tell any Time of Today:")
       sleep(1)
       audio = r.listen(source,phrase_time_limit=3)
    try:
        file = open("reminder_"+str(now.month)+"_"+str(now.day)+".txt","a")
        file.write(r.recognize_google(audio))
        file.close()
    except sr.UnknownValueError:	
       acknowlge("I cannot understand the words I am sorry boss")
    except sr.RequestError as e:
       acknowlge("Please change your tone and speak") 
    

def open_my_search(search_string):
    url = "http://www.google.com/"
    webbrowser.open_new_tab(url)
    sleep(3)
    pyautogui.typewrite(search_string)
    common('enter')
    acknowlge('Please find your deatils')

     
def search_for_me():
    r = sr.Recognizer()
    acknowlge("GO Ahead")
    with sr.Microphone() as source:
       sleep(2)
       audio = r.listen(source,phrase_time_limit=3)
    try:
       open_my_search(r.recognize_google(audio))
    except sr.UnknownValueError:
       acknowlge("I cannot understand the words I am sorry boss")
    except sr.RequestError as e:
       acknowlge("Please change your tone and speak")

switcher = {
        "open Outlook" : openoutlook,
        "open YouTube" : openyoutube,
        "open Chrome": open_chrome,
        "close Chrome" : close_chrome,
        "clone repository": clone_custo,
        "rebase repository":rebase_custo,
        "random name": random_string,
        "select all": hot_key_type,
        "enter"  : enter,
        "mywipro" : open_mywipro,
        "what is my name" : my_name,
        "maximize" : min_maxwindow,
        "minimise" : min_maxwindow,
        "write mode": type_text,
        "how old are you" : age,
        "capture" : print_screen,
        "page down" : page_down,
        "page up": page_up,
        "who are you" : maggiee,
        "Jira status": jira_status,
        "new tab": new_tab,
        "find my route" : show_my_route,
        "Google search": search_for_me,
        "new window" : new_window,
        "suicide" : sucide,
        "set reminder" : reminder,
    }

