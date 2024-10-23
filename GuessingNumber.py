import random

class GuessingGame:
    def __init__(self):
        self.system =random.randint(1,10)
        self.guess =0
    def startGame(self):
        player =input('Guess The Number between 1 to 10:\n')
        if player.isdigit():
            user =int(player)
            self.guess += 1
            if user == self.system:
                print(f"You Have Guessed Correct Number in {self.guess} attempts !")
                quit()
            elif user > self.system:
                print("The guess is Too large !")
            else:
                print("The guess is Too small !")    
        else:
            print("Please Enter  valid number !")

if __name__== "__main__":
   a = GuessingGame()
   print("Welcome To Guessing Game !")
   while True:
       a.startGame()                              
                
        
    
        
                    
        
            
                
                    
