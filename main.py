# Rule Based AI Python Chatbot 

import datetime
import time

name=input("swagat hai, enter your name: ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <=11:
    print("good morning",name)
elif 11 <= presentHour <= 17:
    print("good afternoon",name)
elif 17 <= presentHour <= 20:
    print("good evening,",name)
else:
    print("good night, ",name)



print("Namste!  Welcome to your chatbot")
print(" you can ask me a Basic Question, Type 'bye'to exit from the bot ")

# Chatbot Memory Creation [dictionary of responses]

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "keep going. Every bug of your project makes you a better developer",   # ← FIXED (comma added)
    "happy": "Great to hear that",
    "functions kya hote hai": "jakar chapter 7 padho"
}

# Method/Function to get response of chatbot

def getresponseofbot(userquestion):
    userquestion = userquestion.lower()
    
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]

    return "I am not able to tell that yet. I will learn that soon."



#  Take user input

while True:
    userinput= input("please ask your question:")
    reply= getresponseofbot(userinput)
    print("Bot Response:",reply)

    if "bye" in userinput.lower():
        break
