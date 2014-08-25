# Guess your number
# Player thinks of a number between 1 and 100 and the computer tries to guess it

import random

print "Think of a number between 1 and 100."
print "And I will try to guess it."

tries = 0
guess = ""
high = 100
low = 1
while guess != "c":
    number = random.randrange(low, high)
    print "I think of: ", number
    guess = raw_input("[h]iger, [l]ower, [c]orrect: ")
    if guess == "h":
        low = number +1
        tries += 1
    if guess == "l":
        high = number -1
        tries += 1
  
print "I got it in ", tries, "go's!"


raw_input("\n\nPress the enter key to exit.")
