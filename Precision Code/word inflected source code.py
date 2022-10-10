from pattern.en import singularize
from pattern.en import pluralize
import enchant
from nltk.corpus import wordnet



## creating singular and plural method


## helper method to create singular and plural file

## program initialization goes here 
singular_list = []
plural_list = []
diction = enchant.Dict("en_Us")
display_data=""

def creatPluralSingularFile(word):

    singular = singularize(word)
    
    if word == singular:
        singular_list.append(word)
    else:
        plural_list.append(word)


def spellChecker(word):
     if diction.check(word):
        print("Spelt Correctly\n")
        return True
     else:
        print("Spelt Incorrectly")
        print("Do you mean->> " , diction.suggest(word) , "\n")
        return False

def getPOS(synsetwords):
    ## synsetword is a list[]of word comming from nltk corpus..    
    ## adding verb and now empty list with
    ## with other parth of speach tagin..   
    vList = []
    nList = []
    oList = []

    posList = [pos.pos() for pos in synsetwords]
    for pl in posList:
        if pl == "v":
            vList.append(pl)
        elif pl == "n":
            nList.append(pl)
        else:
            oList.append(pl)

    pos_data = [("Noun" , len(nList)),
    ("Verb" , len(vList)),
    ("Other" , len(oList)) ]
    
    return pos_data


def showUserInputMeaning(isSingle , word):
    print("inflection function")
    # An helper function to detect inflection routing
    # 1. pass user input into routing..
    # 2. get meaning and neccessary details if singular ..
    # 3. if plural stemmatize user input and get meaning ..
    # 4. if incorect word check lema ..
    # 5. if lema exit enter inflation detection ...
    # 6. loop through each word and cut off last index [knivesss]..
    # 7. check new list if word is correct [knives]..
    # 8. create list of inflected words [ssn]..
    # 9. pass user input into routing..
    # 10. pass user input into routing..
    print("is singular : " , isSingle , word)
    syn = wordnet.synsets(word)
    wordLenght = len(syn)
    nCounter = 0
    vCounter = 0 
    lemmaList = []

##  pre information on word passes in
    
    print("\n ********************* DICTIONARY *************************\n")
    print(f"The word {word} as {wordLenght} senses from all SubNet")
    display.delete('1.0' , tk.END)
    display_data = ""
    display_data += f"The word {word} as {wordLenght} senses from all SubNet\n"
    print("\n")

    nNum , vNum , *oNum = getPOS(syn)
    
    print(f"\t ***** As {nNum[1]} sense from {nNum[0]} SubNet ****")
    display_data += f"And {nNum[1]} sense from {nNum[0]} SubNet\n\n"
    if isSingle:
        if nNum[1] != 0:
            display_data += f"\t >>>>> The Noun {word} is Singular <<<<< \n\n"
        for eachWord in syn:
            if eachWord.pos() == "n":
                display_data += f"\t_____________________________________________________________\n"
                lemmaList.clear()                
                for lem in eachWord.lemmas():
                    lemmaList.append(lem.name())
                nCounter = nCounter + 1
                print(f" {nCounter}. {lemmaList[0]}")
                print(">>>> : " , [x for x in lemmaList[1:]])
                print("\t Defination -- : " , eachWord.definition())
                print("\t In Context -- : " , eachWord.examples())
                display_data += f"{nCounter}. {lemmaList[0]}"
                display_data += f" {lemmaList[1:]}\n"
                display_data += f" \t Defination -- : {eachWord.definition()}\n"
                display_data += f"\t In Context -- : {eachWord.examples()}\n"
                 
            elif eachWord.pos() == "v":
                if vCounter == 0:
                    print("\n")
                    print(f"\t ***** As {vNum[1]} sense from {vNum[0]} SubNet ****")
                lemmaList.clear()                
                for lem in eachWord.lemmas():
                    lemmaList.append(lem.name())
                vCounter = vCounter + 1
                print(f" {vCounter}. {lemmaList[0]}")
                print(">>>> : " , [x for x in lemmaList[1:]])
                print("\t Defination -- : " , eachWord.definition())
                print("\t In Context -- : " , eachWord.examples())
##                display_data += f"{vCounter}. {lemmaList[0]}---"
##                display_data += f" {lemmaList[1:]}\n"
##                display_data += f" \t Defination -- : {eachWord.definition()}\n"
##                display_data += f"\t In Context -- : {eachWord.examples()}\n"
            


    if not isSingle:
        if nNum[1] != 0:
            display_data += f"\t >>>>> The Noun {word} is Plural <<<<< \n\n"
        for eachWord in syn:
            if eachWord.pos() == "n":
                display_data += f"\t_____________________________________________________________\n"
                lemmaList.clear()                
                for lem in eachWord.lemmas():
                    lemmaList.append(pluralize(lem.name()))
                nCounter = nCounter + 1
                print(f" {nCounter}. {lemmaList[0]}")
                print(">>>> : " , [x for x in lemmaList[1:]])
                print("\t Defination -- : " , eachWord.definition())
                print("\t In Context -- : " , eachWord.examples())
                display_data += f"{nCounter}. {lemmaList[0]}"
                display_data += f" {lemmaList[1:]}\n"
                display_data += f" \t Defination -- : {eachWord.definition()}\n"
                display_data += f"\t In Context -- : {eachWord.examples()}\n"

            elif eachWord.pos() == "v":
                if vCounter == 0:
                    print("\n")
                    print(f"\t ***** As {vNum[1]} sense from {vNum[0]} SubNet ****")
                lemmaList.clear()                
                for lem in eachWord.lemmas():
                    lemmaList.append(pluralize(lem.name()))
                vCounter = vCounter + 1
                print(f" {vCounter}. {lemmaList[0]}")
                print(">>>> : " , [x for x in lemmaList[1:]])
                print("\t Defination -- : " , eachWord.definition())
                print("\t In Context -- : " , eachWord.examples())
##                display_data += f"{vCounter}. {lemmaList[0]}"
##                display_data += f" {lemmaList[1:]}\n"
##                display_data += f" \t Defination -- : {eachWord.definition()}\n"
##                 display_data += f"\t In Context -- : {eachWord.examples()}\n"

    if nNum[1] != 0:
        display_data += f"\t Cannot make sense of the word {word}\n"

    
        print("THIS IS TOUCH")
    display.insert(tk.END , display_data) 

def idenfityInflation(word , suggest):
    display_data = ""
    display.delete('1.0' , tk.END)
    display_data += f" \n  You Search for  ->>  {user_entry.get().lower()} \n"
    display_data += f" \n  Incorrect spelling : Do you mean! ->>  {suggest} \n"
    w_found = False
    l_word = list(word)
     
    for s in suggest:
        s_word = list(s)

        if l_word == []:
            print("Could not found possible inflection word")
            display_data += f" \n\t Word Not Spelt Correctly\n"
            display.insert(tk.END , display_data)
            break

        if l_word == s_word:
            print("found")
            print(f"you inflate ... : {s}")
            display_data += f" \n\t You Inflate The Word  ----> \"{s}\"\n"
            display.insert(tk.END , display_data)

           
            for i in inflate_letter:
                infl+i

            print(inflate_letter)
            print(f"word is inflate with {infl}")
            display_data += f" \n\n\t You Inflate \"{s}\" with  ----> \"{infl}\"\n"
            print(display_data)
            break
        else:
            print("false")

    else:
         print("word reduce [-1]")
         inf = l_word.pop()
         print(inf)
         print(l_word)
         inflate_letter.append(inf)
         idenfityInflation(l_word , suggest)

    
                       
                
    
    

    
def printWordSemantic():
    print("print ... word meaning...")
    

raw_file = open("words_alpha.txt" , "r")

word_file = raw_file.readlines()
p_word = []
words = word_file[:]
display_data = " "


for word in words:
    p_word.append(word[:-1])
    creatPluralSingularFile(word[:-1])
else:
    print("loop completed")
    print(len(p_word))


print(singular_list[:10])
print(plural_list[:10])
print(len(singular_list))
print(len(plural_list))


runProgram = True
foundInSingular = False
foundInPlural = False
isSingular = False
inflate_letter=[]
infl = ""


def lockUpDiction(event=None):

    # check which file i.e (singular or plural file) word can be find....
    isSingular = False
    display_data = ""
    foundInSingular = True
    foundInPlural = True

    text = user_entry.get()
##    input("Enter a word to search for :")
    print(f"user search for {user_entry.get()}")
    user_input = text.lower()
    
    if user_input == "_exit":
        return

    for word in singular_list:
        if word == user_input:
            print("Word is singular")
            if spellChecker(user_input):
                # call the helper method to display data..
                isSingular = True
            else:
                # call the word inflation algorithm
                suggest = diction.suggest(user_input)
                inflate_letter = []
                infl = ""
                idenfityInflation(user_input , suggest)
                pass
            print("Singularity is assign true")
            isSingular = True
            showUserInputMeaning(True, user_input)
            return
    else:
        foundInSingular = False
        print("\t Word not found in sugular file")

            

    # check for plurality if word not found in singular file....
    for word in plural_list:
        if not isSingular:
            if word == user_input:
                print("Word is plural")
                if spellChecker(user_input):
                    # call the helper method to display data..
                    pass
                else:
                    # call the word inflation algorithm
                    pass
                showUserInputMeaning(False , user_input)
                return
    else:
        foundInPlural = False
       # print("\t Word not found in plural file")


    #second word validation
   

    if not foundInSingular and  not foundInPlural:
       
        if not diction.check(user_input):
            suggest = diction.suggest(user_input)
            print("Incorrect spelling : do you mean->> " , suggest )
##            display_data += f" \n\t Incorrect spelling : Do you mean ->>  {suggest} \n"
            inflate_letter=[]
            infl = ""
            idenfityInflation(user_input, suggest)
           



## START the GUI code section ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
import tkinter as tk

root = tk.Tk()
root.title("Enhanced WordNet (Noun SubNet) Browser 2.0")
sv = tk.StringVar()

frame1 = tk.LabelFrame(root , text="" , padx=5 ,pady=2)
##frame1.grid(row=0, column=0)

frame2 = tk.LabelFrame(root , text="" , padx=0 ,pady=0)
##frame2.grid(row=1, column=0)


def show(event=None):
    print(f"hello {user_entry.get()}")
   

## the first frame data...... 
user_entry = tk.Entry(frame1, width=50 , borderwidth=4)
user_entry.bind('<Return>' , lockUpDiction )
search_button = tk.Button(frame1 , text="Search" , padx=15, pady=4 , command=lockUpDiction)
label = tk.Label(frame1 , text ="Search Word : ")
display = tk.Text(frame2)


label.grid(row=0 , column=0)
user_entry.grid(row=0 , column=1, columnspan=3 , pady=10 , padx=10)
search_button.grid(row=0, column=4)


# createing scrollbar
scroll = tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT , fill = tk.Y)
##scroll.grid(row=0 , column=1 , rowspan=5)
scroll.config(command=display.yview)

print("code section reach here")

# the second frame data.....
display.insert(tk.END , "")
display.config(yscrollcommand=scroll.set)
display.pack()
##display.grid( row=0 , column=0 , columnspan=4)


frame1.pack()
frame2.pack()


root.mainloop()

## END of GUI code..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


##print("\n\n********* program terminated *********")

