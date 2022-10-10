from nltk.corpus import wordnet

syn = wordnet.synsets("dog")

nLenght = 0
vLenght = 0
oLenght = 0


print(f"total sences is {len(syn)}")

def getPOS(synsetwords):
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

    pos_data = [("noun" , len(nList)),
    ("verb" , len(vList)),
    ("others" , len(oList)) ]
    
    return pos_data

print(getPOS(syn))

