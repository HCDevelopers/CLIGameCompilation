@echo off
title Trolled!
color 0A
echo Welcome to Trolled! for HC ----Pinkleton----
echo.
echo Choose what you want to do here:
echo.
echo 1.) Start Game
echo 2.) Exit Game
echo.
set /p var=Set Command: 
if %var%==1 goto Start
if %var%==2 goto exit
:Start
cls
echo You come across an evil troll! What do you do?
echo.
echo 1.) Run Away
echo 2.) Attack
set /p var=Set Command:
if %var%==1 goto Run
if %var%==2 goto exit
:Run
echo Obviously you run, that was a bloody troll!
pause
echo After running away from the evil troll you encounter a glowing chest!
echo.
echo 1.) Open Chest
echo 2.) Leave the Chest
set /p var=Set Command:
if %var%==1 goto Open Chest
if %var%==2 goto exit
:Open Chest
echo You opened the chest
echo.
echo You found the Sword of Trolls! It was forged in the blood of newfags
echo You found the Helmet of Trollzarious! which was worn during the ancient troll battle
echo You found the Chest Plate of Trolltan! It has saved many lives before, and I expect it to save many more
echo You found the Greaves of Trolldrago! Legend says these greaves were forged with actual Troll skin
echo You found the Gloves and Boots of Trollvatha! An ancient mystic troll said to have enchanted their armor with the power to kill trolls
pause
echo Will you equip it?
echo.
echo 1.) Equip
echo 2.) Sell the armor to the troll
set /p var=Set Command:
if %var%==1 goto Equip
if %var%==2 goto exit
pause
:Equip
echo You have equiped the armor!
echo.
echo It is time to make your choice.
echo.
echo 1.) Fight the Troll!
echo 2.) Run Away
set /p var=Set Command:
if %var%==1 goto Fight
if %var%==2 goto exit
pause
:Fight
cls
echo You come up to the troll and it is breathing heavy, you can smell its awful stench from the entrance. The troll spots you and leaps towards you. During its leap the troll swings its might club. You dodge the club and jump forward swinging your new sword which hits the troll in the leg. The troll screams in agony and then enrages itself. It swings again hitting you square on, but thank god for your new armor which produced a barrier that took 99 percent of the damage. After the troll is confused as to why his attack was beaten, you leap onto the club and run up it, leaping to the troll arm and climbing its neck. You then jump once more and fly through the sky as you plummet down stabbing the troll in its eye. The troll then turns to stone. You go back to down, sleep with a whore at the brothel, get an STD, and die.
pause
echo.
echo 1.) I played as a hero and I am ready to leave
set /p var=Set Command:
if %var%==1 goto exit
pause
:exit