
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



    rain = random.randrange(0, 2)
    r1 = random.randrange(0, 4)
    p1_die = 0
    p2_die = 0
    end = 0

    # random  + var . done !
    

    print(" 1P have 100 HP")
    sleep(0.5)
    clear_screen()
    print(" 2P have 150 HP")
    sleep(0.5)
    clear_screen()
    print(" 1P have 60 ATK")
    sleep(0.5)
    clear_screen()
    print(" 2P have 120 ATK")
    sleep(0.5)
    clear_screen()
    print(" 1P have 350 DEF")
    sleep(0.5)
    clear_screen()
    print(" 2P have 0 DEF")
    sleep(0.5)
    clear_screen()
    print(" 1P is DEF Type")
    sleep(0.5)
    clear_screen()
    print(" 2P is ATK Type")
    sleep(0.5)
    clear_screen()
    print(" 1P have (DEF IV) and (MAGIC POWER III)")
    sleep(0.5)
    clear_screen()
    print(" 2P have (ATK II) and (HEATH I)")
    sleep(0.5)
    clear_screen()
    print()
    print()

    def go():

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

        sleep(2)
        clear_screen()

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

        elif answer == "Fire":
            if rain == 1:
                print("Sorry , Now is rainy , so , you cant make a fire")
            elif rain == 0:
                if r1 == 0 or r1 == 1:
                    print("Sorry , The enemy kill your fire .")
                    print()
                    print()
                    print("1P - 15 HP")
                    print("2P - 5 HP")
                    print()
                    sleep(1)
                    print("But 1P have (DEF IV) so , damage of 1P only have 1.3423489563 ...... ")
                elif r1 == 2:
                    print("Fire is good !")
                    print()
                    print()
                    print("1P - 2 HP")
                    print("2P - 75 HP")
                    print()
                    sleep(1)
                    print("But 1P have (MAGIC POWER III) so , damage of 2P is 98.953670432 ...... ")
                elif r1 == 3:
                    print("FIRE FIRE BURN BURN !!!!")
                    print()
                    print()
                    print("1P - 0 HP")
                    print("2P - 179 HP")
                    print()
                    sleep(0.5)
                    print("But 2P have (HEATH I) so , 2P Heath is 10 . Lock 1/3")
                    print()
                    sleep(0.5)
                    print("But 1P have (MAGIC POWER III) so , 2P is died .")

                    clear_screen()

                    print("1P win !!") 
                    p2_die = 1
                    end = 1   






    def go2():                

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

        sleep(2)
        clear_screen()

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

        elif answer == "Fire":
            if rain == 1:
                print("Sorry , Now is rainy , so , you cant make a fire")
            elif rain == 0:
                if r1 == 0 or r1 == 1:
                    print("Sorry , The enemy kill your fire .")
                    print()
                    print()
                    print("1P - 5 HP")
                    print("2P - 15 HP")
                    print()
                    sleep(1)
                elif r1 == 2:
                    print("Fire is good !")
                    print()
                    print()
                    print("1P - 75 HP")
                    print("2P - 2 HP")
                    print()
                    sleep(1)
                elif r1 == 3:
                    print("FIRE FIRE BURN BURN !!!!")
                    print()
                    print()
                    print("1P - 179 HP")
                    print("2P - 0 HP")
                    print()
                    sleep(0.5)
                    print("But 1P have (DEF IV) so , 1P damage only is 36 .")
                    print()
                    sleep(0.5)
                    print("But 2P have (ATK II) so , 1P damage finally is 57 .")

                    clear_screen()

                    print("1P win !!") 
                    p2_die = 1
                    end = 1   




    if p2_die != 1 or p1_die != 1 and end != 1:
        go()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go2()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go2()    
    if p2_die != 1 or p1_die != 1 and end != 1:
        go()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go2()  
    if p2_die != 1 or p1_die != 1 and end != 1:
        go()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go2()    
    if p2_die != 1 or p1_die != 1 and end != 1:
        go()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go2()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go2()    
    if p2_die != 1 or p1_die != 1 and end != 1:
        go()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go2()  
    if p2_die != 1 or p1_die != 1 and end != 1:
        go()
    if p2_die != 1 or p1_die != 1 and end != 1:
        go2()     

                



                


        