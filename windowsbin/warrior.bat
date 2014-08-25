@echo off
title The Warrior's Adventure
color 0A
echo Welcome to The Warrior's Adventure -Pinkleton-
echo This is my second command game, I hope you enjoy!
echo.
echo Choose what you want to do here:
echo.
echo 1.) Start Game
echo 2.) Exit Game
echo.
set /p var=Set Command: 
if %var%==1 goto menu1
if %var%==2 goto exit
pause
:menu1
cls
echo You have started the game!
pause
echo You have just finished the last day of basic training. Congratulations are in order, you are now a warrior! To celebrate your achievement we can have some fun, you decide.
echo 1.) Go to the local tavern and drink
echo 2.) Go to the arena and watch the fights
echo 3.) Refuse to go out and write a letter to your family back in your hometown
set /p var=Set Command:
if %var%==1 goto menu2
if %var%==2 goto menu3
if %var%==3 goto menu4
pause
:menu2
echo.
echo The night starts off just like any night in the tavern, except this time you have reason to be proud. You go to the front of the bar and order a round of the finest mead for all your friends. The night continues with raging stories and brutal drinking, until half morning a drunken man come up to and starts picking a fight. Being a warrior now, what do you want to do?
echo.
echo 1.) Fight the man
echo 2.) Ignore the man
set /p var=Set Command:
if %var%==1 goto menu5
if %var%==2 goto menu6
pause
:menu5
echo.
echo Being the warrior you are, you know that this fight won't last long. You hope out of your seat and throw your glass of mead in his face, the man now furious charger at you. Using your advanced agility you quickly move out of the way and throw a deadly kick into the back of his knee, after the man is on the ground you deliver a devastating chop to his neck. The fight end and you go home.
echo.
echo 1.) Wake up
set /p var=Set Command:
if %var%==1 goto menu7
pause
:menu6
echo.
echo You ignore the man and rush out of the bar, feeling proud of yourself for being the bigger man. The night ends at this point and you go home and sleep
echo.
echo 1.) Wake Up
set /p var=Set Command:
if %var%==1 goto menu7
pause
:menu3
echo.
echo You arrive at the arenas right as the next fight it starting. While you are not the type to gamble, given the special day, you make an exception and place a bet.
echo.
echo 1.) Bet 40Jenny on the Blue Team
echo 2.) Bet 40Jenny on the Red Team
set /p var=Set Command:
if %var%==1 goto menu8
if %var%==2 goto menu9
pause
:menu8
echo.
echo You placed 40Jenny on the blue team and the red teams warrior overpowered the blue team in an instant. You lose 40Jenny and go home with no dinner.
echo.
echo 1.) Wake up hungry
set /p var=Set Command:
if %var%==1 goto menu7
pause
:menu9
echo.
echo You placed 40Jenny on the red team, the teams warrior comes out looking confident. The fight ends quickly with 0.9 on the blue team and 3.1 on the red team. The red team won, and you came back with triple your Jenny. You have a wonderful meal and a flask of mead before going to bed.
echo.
echo 1.) Wake up
set /p var=Set Command:
if %var%==1 goto menu7
pause
:menu4
echo.
echo You decide to end the night without going out, so you come home and write to your family back home. A lot has happened to you. Some of it was good, some of it was bad, and most of it was just average.
echo.
echo 1.) Write a letter about the good things
echo 2.) Write a letter about the bad things
set /p var=Set Command:
if %var%==1 goto menu10
if %var%==2 goto menu11
pause
:menu10
echo.
echo You write a letter about the great things that have happened to you! You tell your family how you miss them and will always love them. When your family receives the letter they send you 15Jenny, which is more than they could ever afford, just so you can have a night out. You think to yourself what great parents.
echo.
echo 1.) Go to bed and wake up the next morning
set /p var=Set Command:
if %var%==1 goto menu7
pause
:menu11
echo.
echo You decide to write about the bad things that happened to you. Your parents get the letter and feel horrible for encouraging you sign up. The sell all there land, trade in the tools, and send you 2,000Jenny. However after doing this your parents take there own lives out of guilt, but you don't find this out till you go home 15 years later.
echo.
echo 1.) Go to bed and wake up the next morning
set /p var=Set Command:
if %var%==1 goto menu7
pause
:menu7
cls
echo You wake up in the morning feeling as though your rest was cut short an hour or two. You slowly get washed up and then change into your new warriors armor. You reflect on what you did last night and think to yourself if you made the right choice. You shrug it off and leave the house. You then encounter your new manager, Barnabas Pinkleton.
echo.
echo 1.) Show respect and take a kneel before Mr Pinkleton
echo 2.) Forget respect and ask directly what your assignment is
set /p var=Set Command:
if %var%==1 goto menu12
if %var%==2 goto menu13
pause
:menu12
echo.
echo Why what a respectful young lad we have here today. For your first day I will start you off with something easy, boars. I want you to go into the woods behind town and bring me the meat of one boar.
echo.
echo 1.) Accept Quest and Proceed to the woods
set /p var=Set Command:
if %var%==1 goto menu14
pause
:menu13
echo.
echo What a rude little brat! For your first I will must start you off with something easy, boars, although with manners like yours you will probably die right off. Go into the woods and bring the meat of one boar
echo.
echo 1.) Accept Quest and Proceed to the woods
set /p var=Set Command:
if %var%==1 goto menu14
pause
:menu14
cls
echo You arrive in the woods after accepting the quest. You have two choices, sit and wait for a boar to pass through, or go deep into the woods to find one yourself.
echo.
echo 1.) Wait for the boar (estimated time 3 hours)
echo 2.) Find the boar yourself (estimated time 30 minutes)
set /p var=Set Command:
if %var%==1 goto menu15
if %var%==2 goto menu15
pause
:menu15
cls
echo You come across a wild boar finally, after all the time you spent on this boar, and now you can kill it. There are many ways to kill a board, but being the warrior you are you charge at it. You unsheathe your sword and jump towards a tree, kicking the tree and launching yourself at an angle towards the boar. In mid flight you swing your sword and take the beasts head.
echo.
echo 1.) Return to Mr Pinkleton
set /p var=Set Command:
if %var%==1 goto menu16
pause
:menu16
cls
echo You have done good bringing me the meat of a boar, I now promote you to level 2! Now don't get cocky yet, you still have a long way to go before reaching the top. Are you ready for the next quest? Oh who am I kidding, its not like you have a choice anymore... Oh wait you didn't know? After you complete your beginners quest you are now the property of your manager. Now go stand post outside the inn, its your turn for guard duty!
echo.
echo 1.) While surprised set out to guard duty.
echo 2.) Kill yourself and be free from being his property
set /p var=Set Command:
if %var%==1 goto menu17
if %var%==2 goto menu18
pause
:menu17
cls
echo You set out for your first time on guard duty, which will probably be just another boring day. It starts early in the morning and you have to wear such heavy armor. You spend the day with the other guards, which is basically finding any excuse to enjoy yourself. However today ends with you barely keeping your eyes open. You go home
echo.
echo 1.) Sleep, you've earned it.
set /p var=Set Command:
if %var%==1 goto menu19
pause
:menu18
cls
echo You try to kill yourself but fail because the doctor revives you, now you are sold into sex slavery where you shall be raped by men everyday until death! Rethink you actions.
echo 1.) GAME OVER! Restart
set /p var=Set Command:
if %var%==1 goto menu1
pause
:menu19
cls
echo You awake in the morning and get ready for another day of guard duty.
echo.
echo 1.) Go to guard duty
echo 2.) Skip guard duty
set /p var=Set Command:
if %var%==1 goto menu20
if %var%==2 goto menu21
pause
:menu21
cls
echo You skipped guard duty and were branded a traitor. Pinkleton sends men out to kill you.
echo.
echo 1.) GAME OVER! Restart
set /p var=Set Command:
if %var%==1 goto menu1
pause
:menu20
echo.
echo You leave the house and take the long walk to your post. You feel bored already, but slightly excited. Almost as if you could feel something would happen today, and how right you were. It seems that board you killed earlier had a mother, a mother who weighs 960lb and is out for blood. You have no choice but to fight it
echo.
echo 1.) Fight
set /p var=Set Command:
if %var%==1 goto menu22
pause
:menu22
cls
echo You start the epic fight the boar. First you order the other guards to circle the boar and attack the legs. After the men have damage the boars legs you run up to the boar and unsheathe two of your daggers, you then plunge the dagger into its leg and start climbing up. It is shaking and thrusting violently at you and now are scared. Overcoming your fear you continue to climb and reach the boars back, you firm yourself onto it and unsheathe your long sword. You start hacking away, and after hundreds of swings the beast drops dead. You are regarded as a hero and promoted to rank 5!
echo.
echo 1.)Pass out and wake up in the hospital
set /p var=Set Command:
if %var%==1 goto menu23
pause
:menu23
cls
echo You wake up in the hosptial, wondering what happened last night. Your head aches and you cringe every time you attempt to remember you feel groggy.
pause
echo That groggy feeling slowly fades away as you realize, I just killed a bloody boar the size of my home! echo Your body feels at though every single step is putting pressure onto your bones, you feel as though the adrenaline rush from fighting used even your bone marrow to help with this fight. You go back to sleep, not awaking for another week.
pause
echo The time has officially past, and now you are feel perky and hot, almost as if you were a whore at the brothel after a good tip. You realize, your level 5. That is only 5 ranks under Pinkleton, soon you won't be a slave, but a slave owner. You go to message board posted infront of where the inn once was, you take a look and see a bounty for you to acquire.
echo 1.) Take the bounty
set /p var=Set Command:
if %var%==1 goto menu24
pause
:menu24
cls
echo Good job on accepting the bounty, you are going after an infamous man known as Boris the Flesh, who is said to have fingers so strong it can rip metal from a blade, flesh from your body, and crush rocks as though they were butter. You gulp and set off.
pause
echo.
echo This is my next break HC. Come back to the thread later for more.
pause
:exit