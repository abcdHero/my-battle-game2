import random
import time
import platform
import subprocess
from time import sleep

def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if platform.system().lower()=="windows" else "clear"

    # Action
    return subprocess.call(command) == 0


print("Wellecome to BATTLE !")
print("You are in Level 1.")
lvplus = input("Are you want to Level UP?") # Yes or No

if lvplus == "Yes":
   print("You don't have enough coins")
elif lvplus == "No":
   print("Ok")
else:
    print("Error 404")
    print("Please restart your computer")
    exit()

clear_screen()    

print("You are Level 1")
print("You want to play online , play with computer or two players ?")
print(" 1:oneline , 2:computer , 3:two players")
print("one , two or three ?")
oct1 = input("1 , 2 or 3 ?")

if oct1 == "1":
   print("loading")
   sleep(0.5)
   clear_screen()
   print("loading.")
   sleep(0.5)
   clear_screen()
   print("loading..")
   sleep(0.5)
   clear_screen()
   print("loading...")
   sleep(0.5)
   clear_screen()  
   print("loading....")
   sleep(0.5)
   clear_screen()
   print("loading.....")
   sleep(0.5)
   clear_screen()
   print("loading......")
   sleep(0.5)
   clear_screen() 
   print("loading")
   sleep(0.5)
   clear_screen()
   print("loading.")
   sleep(0.5)
   clear_screen()
   print("loading..")
   sleep(0.5)
   clear_screen()
   print("loading...")
   sleep(0.5)
   clear_screen()  
   print("loading....")
   sleep(0.5)
   clear_screen()
   print("loading.....")
   sleep(0.5)
   clear_screen()
   print("loading......")
   sleep(0.5)
   clear_screen() 
   print("loading")
   sleep(0.5)
   clear_screen()
   print("loading.")
   sleep(0.5)
   clear_screen()
   print("loading..")
   sleep(0.5)
   clear_screen()
   print("loading...")
   sleep(0.5)
   clear_screen()  
   print("loading....")
   sleep(0.5)
   clear_screen()
   print("loading.....")
   sleep(0.5)
   clear_screen()
   print("loading......")
   sleep(0.5)
   clear_screen() 
   print("Sorry , No one want to play with you.")
   exit()
elif oct1 == "2":
   print("Bug , Error 6720")
   sleep(2)
   exit()
elif oct1 == "3":
   Name1 = input("What is the name of 1P     ")
   Name2 = input("What is the name of 2P     ") # I'll fix that
   print("First player name is " + Name1 + " .")
   print("Second player name is " + Name2 + " .")
   print("allright ?    ")
   allright1 = input("Yes or No ?     ")

   comment = input("your comment")
else:
   exit() # I'll fix that too !   

 

     


