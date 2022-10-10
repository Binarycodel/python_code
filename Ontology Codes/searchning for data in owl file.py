 from owlready2 import *

ontology = get_ontology("newMaizeOntology.owl")
ont = ontology.load()
classes = ont.classes()

count = 0


for clas in list(classes):
    count += 1
    print(f" {count} >>> {clas.}")

print(ont.search(iri = "*Maize*"))
print()
print(ont.search(can_be_maize = "*"))
