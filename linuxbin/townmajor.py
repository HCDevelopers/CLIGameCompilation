#Coded in Python 2.7.3
#By DaPaus

 
import os, sys
from random import randrange

#Determines OS and sets clear command

if sys.platform in ("linux", "linux2"):
    clear = lambda: os.system("clear")
else:
    clear = lambda: os.system("cls")
clear()


def welcome():
    global PlayerName
    print "\n      _________ _______           _       "
    print "      \__   __/(  ___  )|\     /|( (    /|"
    print "         ) (   | (   ) || )   ( ||  \  ( |"
    print "         | |   | |   | || | _ | ||   \ | |"
    print "         | |   | |   | || |( )| || (\ \) |"
    print "         | |   | |   | || || || || | \   |"
    print "         | |   | (___) || () () || )  \  |"
    print "         )_(   (_______)(_______)|/    )_)"
    print "                                          "
    print "    _______  _______ _________ _______  _______ "
    print "   (       )(  ___  )\__    _/(  ___  )(  ____ )"
    print "   | () () || (   ) |   )  (  | (   ) || (    )|"
    print "   | || || || (___) |   |  |  | |   | || (____)|"
    print "   | |(_)| ||  ___  |   |  |  | |   | ||     __)"
    print "   | |   | || (   ) |   |  |  | |   | || (\ (   "
    print "   | )   ( || )   ( ||\_)  )  | (___) || ) \ \__"
    print "   |/     \||/     \|(____/   (_______)|/   \__/"
    print "\n   ============================================="
    print "   Created by DaPaus v1.2"
    raw_input("\n           PRESS ENTER TO CONTINUE")
    clear()
    PlayerName = raw_input("\nWhat is the name of your character?: ")
    clear()
    print "Welcome %s," % PlayerName
    print "\nYou have been choosen as the leader of a town"
    print "in the middle of nowhere. You will have to do "
    print "your best to make an excellent settlement."
    print "\nAfter 30 days the town will be evaluated and the"
    print "game ends... Good luck!"
    raw_input("\n           PRESS ENTER TO CONTINUE")
    clear()

def day():
    global Day
    global Population
    global Production
    global Goods
    global Money
    global CityName
    global Good_Price
    global CityLevel

    Money = Money + (Population * randrange(1,5) )
    Goods = Goods + (Population *(Production / 10.0) )
    Good_Price = randrange(5,15)
    Goods = int(Goods)#Makes Goods an integer
    clear()
    print " %s,  DAY %d\n" % (CityName, Date)
    
    #Population levels
    done1 = False
    done2 = False
    done3 = False
    if (Population > 50):
        if (done1 == False):
            print "\n%s reached more then 50 residents" % CityName
            print "%s is now a Town" %CityName
            done1 = True
            CityLevel = "Town"
            raw_input("\n           PRESS ENTER TO CONTINUE")
            clear()
    elif (Population > 100):
        if (done2 == False):
            print "\n%s reached more then 100 residents" % CityName
            print "%s is now a City" %CityName
            done2 = True
            CityLevel = "City"
            raw_input("\n           PRESS ENTER TO CONTINUE")
            clear()
    elif (Population > 150):
        if (done3 == False):
            Money = Money + 500
            print "\n%s reached more then 150 residents" % CityName
            print "%s is now a Metropolis" %CityName
            print "\nYou earned 500 Coins by achieving this"
            done3= True
            CityLevel = "Metropolis"
            raw_input("\n           PRESS ENTER TO CONTINUE")
            clear()

    #Chek for Events
    if (Date == 1):
        event_day1()
    elif (Date == 5):
        event_day5()
    elif (Date == 15):
        event_day15()
    elif (Date == 31):
        event_day31()
    menu()

#Menu and its functions
def menu():
    global CityName
    global Date
    clear ()
    print " %s,  DAY %d\n" % (CityName, Date)
    print "        MAIN MENU"
    print "       ------------"
    print "     1) Statistics"
    print "     2) Shop"
    print "     3) End day"
    print "     4) Quit Game"
    choice = raw_input("Choose an option: ")
    if choice.isdigit():
        choice = int(choice)

    if (choice==1):
        stats()
    elif (choice==2):
        shop()
    elif (choice==3):
        end_day()
    elif (choice==4):
        quit_game()
    else:
        menu()

def stats():
    global Day
    global Population
    global Production
    global Goods
    global Money
    global CityName
    global CityLevel
    clear()
    print "\n\n       Records of %s" % CityName
    print "     ----------------------"
    print "   City Level: %s" % CityLevel
    print "   Population: %d" % Population
    print "   %d Coins" % Money
    print "   Production: %r" % (Production/10.0)
    print "   %d Goods" % Goods
    raw_input("\n           PRESS ENTER TO CONTINUE")
    menu()
    

def shop():
    global Goods
    global House
    global Population
    global Factory
    global Production
    global Money
    global Good_Price
    clear()
    print " %d COINS" % Money 
    print "\n           Shopping Menu"
    print "           -------------"
    print "     1) Buy House      150 Coins"
    print "     2) Buy Factory    250 Coins"
    print "     3) Sell Goods     %r Coins" % Good_Price
    print "     4) Back to menu"
    choice = raw_input("Choose an option: ")
    if choice.isdigit():
        choice = int(choice)
    if (choice==1):
        if (Money < 150):
            print "\n Not enough coins!\n"
            shop()
        else:
            House = House + 1
            Population = Population + randrange(4,6)
            Money = Money - 150
            shop()
    elif (choice==2):
        if (Money < 250):
            print "\n Not enough coins!\n"
            shop()
        else:
            Factory = Factory + 1
            Production = Production + 1
            Money = Money - 250
            shop()
    elif (choice==3):
        Money = Money + (Good_Price * Goods)
        Goods = 0
        shop ()
    elif (choice==4):
        menu()
    else:
        shop()

def end_day():
    global Date
    clear()
    print " It becomes night and everyone goes to bed and"
    print " waits for a new day to come... "
    Date = Date + 1
    raw_input("\n           PRESS ENTER TO CONTINUE")
    day()

def quit_game():
    clear()
    print "Nothing will be saved and you will have to restart the game!"
    choice = raw_input("\nAre you sure you want to quit? (y/n) ")
    if (choice=="y"):
        print "\nThanks for playing!"
        raw_input("\n           PRESS ENTER TO CONTINUE")
        sys.exit()
    elif (choice=="n"):
        menu()
    else:
        quit_game()

#Event Functions


#Day 1 - Asks the player for it's town name
def event_day1():
    global CityName
    global PlayerName
    global Money
    Money = 500
    print "It's the first day of your journey and your people"
    print "ask you to name your town. So that everyone will "
    print "know how it's called."
    CityName = raw_input("\nSo what's the name of the town?: ")
    print "\nSo it's official %s is the the major of %s!" % (PlayerName, CityName)
    print "May it grow to the biggest city known to mankind!"

def event_day5():
    global CityName
    global PlayerName
    global Goods
    global Money
    print "This morning a messenger from a town named Acirema"
    print "arrived an asked you for a favor: \"The people in"
    print "Acirema are starving, and we ask you to give some of"
    print "your goods to us. Not for free ofcourse! We buy all "
    print "your goods for 20 Coins each.\""
    print "\nYou have %d Goods." % Goods
    choice = raw_input("Would you like to sell your goods? (y/n) ")
    if (choice=="y"):
        Money = Money + (Goods * 20)
        Goods = 0
        clear()
        print "The people of Acirema thank you!"
        raw_input("\n   PRESS ENTER TO CONTINUE")
    else:
        clear()
        print "The messenger of Acirema wanders of..."
        raw_input("\n   PRESS ENTER TO CONTINUE")

def event_day15():
    global CityName
    global Population
    global Production
    global Factory
    print "Some people complain about air polution. We will have"
    print "to destroy 2 factories otherswise 30 people will leave. "
    choice = raw_input("Destroy the factories? (y/n): ")
    if (choice=="y"):
        Factory = Factory - 2
        Production = Production - 0.2
        Population = Population + 10
        clear()
        print "The townfolks are happy that you listen to them."
        print "10 more people moved to your city"
        raw_input("\n   PRESS ENTER TO CONTINUE")
    else:
        clear()
        print "The townpeople are mad and leave!"
        Population - 30
        raw_input("\n   PRESS ENTER TO CONTINUE")

def event_day25():
    global House
    global Money
    global Population
    global Goods
    global CityName
    if (House > 5):
        print "This night a huge fire destroyed 5 houses. "
        print "30 residents are homeless now. Pay 600 Coins"
        print "for the repairments or else the residents will"
        print "leave..."
        choice = raw_input("\nPay 600 Coins? (y/n): ")
        if (choice=="y"):
            if (Money > 599):
                Money = Money - 600
                Goods = Goods + 25
                "The people are thankfull and give you 25 Goods"
                raw_input("\n   PRESS ENTER TO CONTINUE")
            else:
                Population = Population - 30
                House = House - 5 
                "The people aren't pleased and leave"
                raw_input("\n   PRESS ENTER TO CONTINUE")   
        else:
            Population = Population - 30
            House = House - 5 
            "The people aren't pleased and leave"
            raw_input("\n   PRESS ENTER TO CONTINUE")
    else:
        print "There is an economical crisis in the town Eporue"
        print "and the residents of Eporue are coming to %s." % CityName
        print "Give them 1000 Coins and they will build own houses."
        choice = raw_input("\nPay 1000 Coins? (y/n): ")
        if (choice=="y"):
            if (Money > 1000):
                Money = Money - 1000
                House = House + 9
                Population = Population + 40
                "The new residents are pleased with their welcome"
                raw_input("\n   PRESS ENTER TO CONTINUE")
        else:
            if (Goods > 10):
                Goods = Goods - 10
                print "The group where mad that they didn't recieve"
                print "any money and stole 10 Goods"
                raw_input("\n   PRESS ENTER TO CONTINUE")
            else:
                print "They ran away mad."
                raw_input("\n   PRESS ENTER TO CONTINUE")

def event_day31():
    global House
    global Population
    global Factory
    global Money
    global PlayerName
    global CityName
    clear()
    Score = (House * 5) + round(Population/0.1) + round(Money/0.1) + (Factory * 10)
    print "                     End Game"
    print " ============================================="
    print "     Major %s of the %s %s" % (PlayerName,CityLevel,CityName)
    print "\n     TOTAL SCORE: %d" % Score     
    print " ============================================="
    print "                 THANKS  FOR PLAYING"
    print "\n\n              CREATED BY DAPAUS"
    print "\n               FOR HACKCOMMUNITY.COM"
    raw_input("\n   PRESS ENTER TO CONTINUE")
    sys.exit()

#Flow of execution
Date = 1
Population = 20
Production = 1
Goods = 0
Money = 500
House = 5
Factory = 0
Good_Price = 1
CityName = "Town"
PlayerName = "Name"
CityLevel = "Settlement"

welcome()
day()
