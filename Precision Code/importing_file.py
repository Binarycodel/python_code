from pattern.en import singularize
##  IMPORTING WORD FILE

## helper method to create singular and plural file

singular_list = []
plural_list = []

def creatPluralSingularFile(word):
    if word == singularize(word):
        singular_list.append(word)
    else:
        plural_list.append(word)


print(singular_list[:10])
print(plural_list[:10])



raw_file = open("words_alpha.txt" , "r")

word_file = raw_file.readlines()
p_word = []
words = word_file[:]


user_input = input("Enter a word : ")

for word in words:
    p_word.append(word[:-1])
    if user_input == word[:-1]:
        print("user entery found in index : " , word[:-1])
        break
else:
    print("not found")
    
    
print("\t\t this is the new words")
print("\n")
#print(p_word)
print(len(p_word))
