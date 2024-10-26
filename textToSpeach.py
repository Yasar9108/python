import pyttsx3


def T2Speach():
    Speach =pyttsx3.init()
    Speach.say(input("Enter The Text You Want To Convert :\n"))
    Speach.runAndWait()
    

if __name__ == "__main__":
    try:
       T2Speach()
    except Exception as e:
        print("Some Thing went Wrong  !")   