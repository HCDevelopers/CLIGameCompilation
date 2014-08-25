#Coded in Python 2.7.3
#By DaPaus

from random import randrange

def welcome():
    global PlayerName
    print "\n\n    _________ _______           _       "
    print "    \__   __/(  ___  )|\     /|( (    /|"
    print "       ) (   | (   ) || )   ( ||  \  ( |"
    print "       | |   | |   | || | _ | ||   \ | |"
    print "       | |   | |   | || |( )| || (\ \) |"
    print "       | |   | |   | || || || || | \   |"
    print "       | |   | (___) || () () || )  \  |"
    print "       )_(   (_______)(_______)|/    )_)"
    print "                                        "
    print "  _______  _______ _________ _______  _______ "
    print " (       )(  ___  )\__    _/(  ___  )(  ____ )"
    print " | () () || (   ) |   )  (  | (   ) || (    )|"
    print " | || || || (___) |   |  |  | |   | || (____)|"
    print " | |(_)| ||  ___  |   |  |  | |   | ||     __)"
    print " | |   | || (   ) |   |  |  | |   | || (\ (   "
    print " | )   ( || )   ( ||\_)  )  | (___) || ) \ \__"
    print " |/     \||/     \|(____/   (_______)|/   \__/"
    print " "
    print " ============================================="
    print " Created by DaPaus v1.0"
    
    raw_input("\n           PRESS ENTER TO CONTINUE")
    PlayerName = raw_input("\n\nWhat is the name of your character?: ")
    print " ============================================="
    print "Welcome %s," % PlayerName
    print "\nYou have been choosen as the leader of a town"
    print "in the middle of nowhere. You will have to do "
    print "your best to make an excellent settlement."
    print "\nAfter 30 days the town will be evaluated and the"
    print "game ends... Good luck!"
    raw_input("\n           PRESS ENTER TO CONTINUE")
    print "\n\n ============================================="

def day():
    global Day
    global Population
    global Production
    global Goods
    global Money
    global CityName
    global Good_Price

    Money = Money + (Population * 3)
    Goods = Goods + round(Population * Production)
    Good_Price = randrange(5,15)

    print "%s,  DAY %d\n" % (CityName, Date)
    if (Date == 1):
        event_day1()
    elif (Date == 5):
        event_day5()
    elif (Date == 15):
        event_day15()
    elif (Date == 31):
        event_day31()
    menu()



        
#MENU and fuctions
def menu():
    print " ============================================="
    print "\n\n         MENU"
    print "         ------"
    print "     1) Statistics"
    print "     2) Shop"
    print "     3) End day"
    print "     4) Quit Game"
    choice = input("\nChoose an option: ")
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
    print " ============================================="
    print "\n\n       Records of %s" % CityName
    print "     ----------------------"
    Production = "{0:.2f}".format(Production)
    print "   Population: %d" % Population
    print "   %d Coins" % Money
    print "   Production: %r" % Production
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
    print " ============================================="
    print " %d COINS" % Money 
    print "\n           Shopping Menu"
    print "           -------------"
    print "     1) Buy House      150 Coins"
    print "     2) Buy Factory    250 Coins"
    print "     3) Sell Goods     %r Coins" % Good_Price
    print "     4) Back to menu"
    choice = input("\nChoose an option: ")
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
            Production = Production + 0.1
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
    print " ============================================="
    print " It becomes night and everyone goes to bed and"
    print " waits for a new day to come... "
    Date = Date + 1
    raw_input("\n   PRESS ENTER TO CONTINUE")
    day()

def quit_game():
    print " ============================================="
    choice = raw_input("\nAre you sure you want to quit? (y/n) ")
    if (choice=="y"):
        print "\nThanks for playing!"
        raw_input("\n   PRESS ENTER TO CONTINUE")
    elif (choice=="n"):
        menu()
    else:
        quit_game()
   
#Events

#Day 1 - Asks the player for it's town name
def event_day1():
    global CityName
    global PlayerName
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
    choice = raw_input("Would you like to sell your goods? (y/n)")
    if (choice=="y"):
        Money = Money + (Goods * 20)
        Goods = 0
        print "The people of Acirema thank you!"
        raw_input("\n   PRESS ENTER TO CONTINUE")
    else:
        print "Oh okay..."
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
        print "The townfolks are happy that you listen to them."
        print "10 more people moved to your city"
        raw_input("\n   PRESS ENTER TO CONTINUE")
    else:
        print "The townpeople are mad and leave!"
        Population - 30
        raw_input("\n   PRESS ENTER TO CONTINUE")


def event_day31():
    global House
    global Population
    global Factory
    global Money
    global PlayerName
    global CityName
    Score = (House * 5) + round(Population/0.1) + round(Money/0.1) + (Factory * 10)
    print "                     End Game"
    print " ============================================="
    print "     Major %s of the city %s" % (PlayerName,CityName)
    print "\n     TOTAL SCORE: %d" % Score     
    print " ============================================="
    print "                 THANKS FOR PLAYING"
    raw_input("\n   PRESS ENTER TO CONTINUE")
    print "\n\n             CREATED BY DAPAUS"
    print "\n             FOR HACKCOMMUNITY.COM"
    
    
#Flow of execution
Date = 1
Population = 20
Production = 0.1
Goods = 0
Money = 500
House = 5
Factory = 0
Good_Price = 1
CityName = "Town"
PlayerName = "Name"

welcome()
day()
