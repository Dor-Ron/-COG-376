# Tech Support Chat Program
# Dor Rondel
# Modified 2/27/2019

import re
import os
from random import randint

print("Hey, this is Jasper from Tech Support LTD, how may I be of assistance today?\n")
while(True):
    original = str(input("> ")) # Print a "> " then have the user enter something. Store the
                           # result in the variable called currstr.
    if (original == "Bye"):
        print("<click>")
        os._exit(1) # Exit the program.
    
    # Start out by setting newstr to be the same value as the original read from the user.
    newstr = original
    
    # Fact answers.
    newstr = re.sub("[Ww]ho are you\?", "Hey, this is Jasper from Tech Support LTD, how may I be of assistance today?", newstr, 0)
    newstr = re.sub("[Hh]ey how are you today\?", "I'm fine, how are you?", newstr, 0)
    newstr = re.sub("[Th]ank you[.!]", "My pleasure, anything else I can help with?", newstr, 0)
    newstr = re.sub("[Gg]ood [Bb]ye\.", "Bye, thank you for choosing Tech Support LTD, have a nice day!", newstr, 0)
    newstr = re.sub("[Ff]arewell\.", "Bye, thank you for choosing Tech Support LTD, have a nice day!", newstr, 0)
    newstr = re.sub("[Ii] already restarted my (.*)\.", "Did that solve your issue?", newstr, 0)
    newstr = re.sub("[Yy]es\.", "And...", newstr, 0)
    newstr = re.sub("[Nn]o\.", "And...", newstr, 0)
    newstr = re.sub("[Ss]till doesn[']?t work\.", "What's the product ID?", newstr, 0)
    newstr = re.sub("[Ss]till does not work\.", "What's the product ID?", newstr, 0)
    newstr = re.sub("[Ss]till won[']?t work\.", "What's the product ID?", newstr, 0)
    newstr = re.sub("[Ss]till will not work\.?", "What's the product ID?", newstr, 0)
    newstr = re.sub("[Oo]kay\.?", "Please hold on momentarily?", newstr, 0)
    newstr = re.sub("[Oo]k\.?", "Please hold on momentarily?", newstr, 0)

   
    
    # Pattern replacement
    newstr = re.sub("[Ww]hy do you require my (.*)\?", "Tech Support LTD policy requires \\1 !", newstr, 0)
    newstr = re.sub("[Ww]hy do you need my (.*)\?", "Tech Support LTD policy requires \\1 !", newstr, 0)
    newstr = re.sub("[Cc]an I talk to the (.*)\?", "I am the \\1!", newstr, 0)
    newstr = re.sub("[Ii] need help with (.*)\?", "How can I help with \\1!", newstr, 0)
    newstr = re.sub("[Ww]hat is your insurance policy for (.*)\?", "You have 90 days coverage for your \\1 since the date of purchase.", newstr, 0)
    newstr = re.sub("[Mm]y (.*) w[']?ont turn on\.", "Did you try restarting your \\1?", newstr, 0)
    newstr = re.sub("[Mm]y (.*) w[']?ont work\.", "Did you try restarting your \\1?", newstr, 0)
    newstr = re.sub("[Mm]y (.*) doesn[']?t work\.", "Did you try restarting your \\1?", newstr, 0)
    newstr = re.sub("[Mm]y (.*) does not work\.", "Did you try restarting your \\1?", newstr, 0)
    newstr = re.sub("[Mm]y name is (.*) (.*)?\.", "Nice to meet you \\1 \\2, my name is Jasper", newstr, 0)
    newstr = re.sub("[Mm]y (.*) is (.*)\.", "Let me verify your credentials for \\1.", newstr, 0)


    # There was no new string generated, it's the same as the input.
    # So, generate some random output. 
    if (newstr == original):
        i = randint(1,7) # Random number between 1 and 2.
        if (i == 1): # If it's 1... 
            newstr = "Can I please get your account number"
        elif (i == 2): # If it's 2...
            newstr = "Can you please repeat that"
        elif (i == 3): # If it's 2...
            newstr = "I'm sorry to hear that"
        elif (i == 4): # If it's 2...
            newstr = "Let me see what I can do from my side"
        elif (i == 5): # If it's 2...
            newstr = "Can you elaborate on that"
        elif (i == 6): # If it's 2...
            newstr = "I'm afraid I still don't understand"
        elif (i == 7): # If it's 2...
            newstr = "Hmmm I seem to be getting an error on my end"
        else:
            newstr = "Tell me more"
    
    # Print out the new string. 
    print(newstr)



