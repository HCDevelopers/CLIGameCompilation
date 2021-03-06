#!/usr/bin/env python
import subprocess
import os

def print_title():
	print('''
************************************************************************
*   _  _ ____ ____ _  _ ____ ____ _  _ _  _ _  _ _  _ _ ___ _   _      *
*   |__| |__| |    |_/  |    |  | |\/| |\/| |  | |\ | |  |   \_/       *
*   |  | |  | |___ | \_ |___ |__| |  | |  | |__| | \| |  |    |        *
*                                                                      *
*____ ____ _  _ ____    ____ ____ _  _ ___  _ _    ____ ___ _ ____ _  _*
*| __ |__| |\/| |___    |    |  | |\/| |__] | |    |__|  |  | |  | |\ |*
*|__] |  | |  | |___    |___ |__| |  | |    | |___ |  |  |  | |__| | \|*
*                                                                      *
*                       <www.Hackcommunity.com>                        *
************************************************************************
                             Windows-Version
	''')

def print_menu():
	print("Choose your game:")
	print
	print("1. DeBaseMaster by H4R0015K")
	print("2. Guess Your Number by chmod")
	print("3. Find The Door by Xe.4")
	print("4. Simple Lua Text Adventure by JesseH")
	print("5. Paper Scissor Rock by Ex094")
	print("6. Hangman by Ex094")
	print("7. Rock Paper Scissors by Jacob")
	print("8. Town Major by Dapaus")
	print("9. Tic-Tac-Toe by Psycho_Coder")
	print("10. Number Magic Game by Psycho_Coder")
	print("11. Trolled by PInkleton")
	print("12. The Warrior's Adventure by PInkleton")
	print

def start_game(gamenr):
	cmd = ["", "", "", "", "", "", "java -jar ", "", "", "", "", ""]
	files = ["debasemaster.py", "guessnr.py", "findthedoor", "luatextrpg.lua", "rockpaperscissor.py", "hangman.py", "RPS.jar", "townmajor.py", "tictactoe", "numbermagic", "Trolled.bat", "warrior.bat"]
	di = os.path.dirname(os.path.abspath(__file__))
	subprocess.call(cmd[gamenr-1] + "\"" + di + "\"" + "\\" + files[gamenr-1], shell=True)

def main():
	print_title()
	print_menu()
	choice = raw_input("Your choice (type exit to leave): ")
	if choice.isdigit() and int(choice) <= 12 and int(choice) > 0:
		start_game(int(choice))
	else:
		if choice != "exit":
			main()	

main()
