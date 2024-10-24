import pyttsx3

def TextTospeach():
    speak =pyttsx3.init()
    speak.say(input("Enter The text \n"))
    speak.runAndWait()
    
TextTospeach()    