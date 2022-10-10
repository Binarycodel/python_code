from owlready2 import*

#ont = get_ontology("C:\\Users\\binary\\Videos\\MY PYTHON CLASS\\PythonCode\\Ontology Codes\\newMaizeOntology.owl")
ont = get_ontology("newMaizeOntology.owl")
ont.load()
print(ont.Climate)
ont_class = ont.classes()
ont_Oproperty = ont.object_properties()
##print(list(ont_class))
print(ont.base_iri)
i = 0

print("THE CLASSES IN THE ONTOLOGY")
      
for cla in list(ont_class):
    i=i+1
    print(f"{i} >> {cla}")


print("THE OBJECT PROPERTY IN THE ONTOLOGY")
for ob in list(ont_Oproperty):
    i=i+1
    print(f"{i} >> {ob}")
    


