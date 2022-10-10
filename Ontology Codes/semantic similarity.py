from nltk.corpus import wordnet

word = input("enter a word: " , )

base_domain = "agriculture.n.01"

sys = wordnet.synsets(word)

def comparator(data_one , data_two):
    base_data = wordnet.synset(data_one)
    for w in data_two:
        print(w.wup_similarity(base_data))
        

comparator(base_domain , sys)
