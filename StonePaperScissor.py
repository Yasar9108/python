import random

def start():
    totalattempts =0
    userattempts = 0
    systemattempts = 1
    user_name =input("Enter Your name ! : \n")
    while True:
        totalattempts += 1
        system =random.randint(1,3)
        print(f"level :{totalattempts} ")
        user = int(input("1 STone 2 Paper 3 Scissor : \n"))
        if user > 3:
            print("Please restart Game Enter valid number :")
            break
        if totalattempts==5:
            quit()
        elif user == 1 and system ==3 or user ==2 or system == 1 or user ==3 and system ==2:
            print("You won !")
            print(f"System choice is {system}")
            userattempts += 1
            if userattempts >=3:
                print(f"{user_name}: You won , TotalLeveles:{totalattempts} : You Won {userattempts}")
                break
        elif user==system:
            userattempts+=1
            systemattempts+=1
            print("draw")    
        else:
            systemattempts += 1
            print(f" systemchoice :{system}  system won")
            if systemattempts >=3:
               print(f"System won  ,total levels :{totalattempts} : system won :{systemattempts}")
               break            

            
            
if __name__ == "__main__":
    try:
        print('Welcome to Rock Paper Scissor game !:')
        user =input('Enter start or 1 to start game :\n')
        if user.startswith("start".lower()) or user.startswith("1"):
            start()
        else:
            print("Have nice day !")
    except Exception as e:
        print("Some thing went wrong ! Try again !")                 
            
                
            