# Correct word checker

import enchant

diction = enchant.Dict("en_Us")

run = True

while run == True:
    data = input("Enter a word : ")
    
    if data == "exit()":
        break

    if diction.check(data):
        print("Correct Word\n")
    else:
        print("Incorrect word\n")
