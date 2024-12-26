import speech_recognition as sr
import pyttsx3 as pt
import time ,schedule
import word2num as w2n
import threading
import webbrowser

# Speech To Text Engine.
recognizer = sr.Recognizer()

def listen(sourse):
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    My_text = recognizer.recognize_google(audio).lower()
    return My_text

# Text To Speech Engine.
tts_engine = pt.init()

# decrease the speed of tts_engine
tts_engine.setProperty("rate", 135)

# this fun to say what the user say
def say(text):
    if text is not None:
        tts_engine.say(text)
        tts_engine.runAndWait()
        return
    tts_engine.say(text)
    tts_engine.runAndWait()
    return

# convert word to text.
def word_to_text(word):
    try:
        num = w2n.word2num(word)
        return int(num)
    except Exception as ee:
        print(f"Error occuried {ee}")

# to schedule the task
def schedule_task(job, repetition, period):
    def task():
        say(job)
    if "second" in period:
        schedule.every(word_to_text(repetition)).seconds.do(task)
    elif "minute" in period:
        schedule.every(word_to_text(repetition)).minutes.do(task)
    elif "hour" in period:
        schedule.every(word_to_text(repetition)).hours.do(task)
    elif "day" in period:
        schedule.every(word_to_text(repetition)).day.do(task)

# this fun for say all tasks to user
def say_all_tasks():
    tasks = schedule.get_jobs()
    if tasks:
        say('Here are your schedule tasks: ')
        for index,task in enumerate(tasks, start = 1):
            say(f'Task {index}: {task} ,repeats every {task.interval} {task.unit}')
    else: 
        say('you have no tasks scheduled')

# this fun for run the schedule
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# this fun for run the schedule tasks in separated thread
def start_schedule_thread():
    thread = threading.Thread(target = run_schedule)
    thread.start()

# to make a thread for running the schedule
start_schedule_thread()

# this fun for search on google
def search_google(query):
    # to check if the path is true
    try:
        google_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        url = f'https://www.google.com/search?q={query}'
        browser = webbrowser.get(google_path)
        browser.open(url)
    # if the path not true we will open the deafult browser
    except webbrowser.Error :
        webbrowser.open(url)

first_running = True
while True:
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source:

            # ask for user's name 
            while first_running:
                # introductiot
                say("Welcome at APlus voice assistant.")
                say("Hello ,what's your name: ")
                user_name = listen(source)
                # to check if the user enter his name.
                if user_name:
                    say(f"hello, {user_name}")
                    first_running = False
                else:
                    say("i can't catch your name, please try again")

            say("I can help you organize your schedule and search online")
            say("if you want to seach on google say search on google.")
            say("if you want to organize your schedule say schedule.")
            say("if you want to exit the program say finally")
            say(f"how can i help you?")
            my_text = listen(source)
            time.sleep(1)

            # if user say search on google.
            if 'search' in my_text or 'google' in my_text:
                say("what is the website that you want to search on google")
                listen(source)
                query = time.sleep(1)
                search_google(query)

            # if user say schedule.
            elif 'schedule' in my_text or 'organize' in my_text:
                running = True
                while running:
                    say("what is the task that you want to add to your schedule.")
                    job = listen(source)
                    time.sleep(1)
                    say("How many times do you want to repeat this task")
                    repetition = listen(source)
                    time.sleep(1)
                    say("Is this task every second, minute, hour or day?")
                    period = listen(source)
                    time.sleep(1)
                    schedule_task(job, repetition, period)
                    say("The task has been registered successfully")
                    say("if you want to listen to your all tasks say tasks.")
                    check = listen(source)
                    if check == 'tasks':
                        say_all_tasks()
                    say("if you want to stop say close.")
                    my_text = listen(source)
                    if my_text == "close":
                        running = False

            # if user want to stop the chat.
            elif my_text in ['stop', 'finally', 'finish', 'end']:
                break

            # if the engine can't understand what the user say.
            else:
                say("i can't understand what you say please try again.")
    except:
        pass

say("thank you for using A+ voice assistant.")
say(f"goodbye {user_name}")