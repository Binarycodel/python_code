from pattern.en import singularize
from pattern.en import pluralize




##print("user input : " , user_input)
##singular = singularize(user_input)
##print("singularize:" , singular)
##plural = pluralize(user_input)
##print("pluralize:" , plural)


while True :
    user_input = input("words: ")

    singular = singularize(user_input)
    plural = pluralize(user_input)

    print(f"Plural rep : {plural}")
    print(f"singular rep : {singular}")
    
    if user_input == singular:
        print(f"{user_input} : is singular word")
        precise_word = singular
        
    elif user_input == plural:
        print(f"{user_input} : is plural word")
        precise_word = plural
        
    elif user_input == "_exit":
        break
        
    else:
        print(f"{user_input} : is incorrect...")


    print(precise_word)







## CREATING A TURPLE LIST OF SINGULAR AND PLURAL WORDS


##dictionary = set()
##
##for word in p_word:
##    if word == singularize(word):
##        print(f"{word} is singular word")
##        dictionary.add((word , pluralize(word)))
##    else:
##        print(f"{word} is plural word")
##        dictionary.add(( singularize(word) , word ))
##
##dictionary = list(dictionary)
##print(list(dictionary))
