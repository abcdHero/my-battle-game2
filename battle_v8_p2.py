
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

def play2():

    print(" You can choose : ")
    print()
    print("Bow")
    print("Jump")
    print("Fire")
    print("Attack")
    print()
    print("* * You cant put fire on rainy * *")
    print()
    print("* * Fire have 50 % chance to die * *")
    print()

    answer = input()

    if answer == "Bow":

        for j in range(20):
            clear_screen()
            hero_char = 'O+< (|'
            hero_char2 = "O+<"
            hero_char3 = "O+< HA HA"
            hero_char4 = "0+< OUCH"
            middle_thing = ''
            for i in range(20):
                if j == i:
                    middle_thing += '-->'
                else:
                    middle_thing += ' '
            print(hero_char + middle_thing + hero_char2)
            time.sleep(0.05)  

        clear_screen()
        print(hero_char3 + middle_thing + hero_char4)   

    elif answer == "Jump":
        x = 0 
        

        while x != 5:
            print("O")
            print("+")
            print("^")
            print()
            print("O")
            print("+")
            print("^")

            sleep(0.25)
            
            clear_screen()
            print()
            print("O")
            print("+")
            print("^")
            print("0")
            print("+")
            print("^")

            sleep(0.25)

            clear_screen()

            x = x + 1


        




play2()