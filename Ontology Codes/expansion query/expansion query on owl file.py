from owlready2 import *

## GETTING ONTOLOGY FILE
farm_onto = get_ontology("maizeFarmingOntology_MODIFY2_VALIDATION.owl").load()
#farm_onto = get_ontology("https://staff.futminna.edu.ng/website_home.php?id2=82a324332344/maizeFarmingOntology_MODIFY2_VALIDATION.owl").load()
#farm_onto = get_ontology("newMaizeOntology.owl").load()
#print(farm_onto.AnimalType)

# INITIALIZING SEED VARIABLE
seed_variable = ["maize" , "soil" , "fertilizer" , "irrigation"]

# GETTING USER INPUT
##user_query = input("Enter Query : " , )
##print(user_query)


# GETTING ONTOLOGY CONCECPT----- CLASSESS ...
ont_concept = list(farm_onto.classes())
print(ont_concept[0:10])
concept_size = len(ont_concept)
print(f"Farm ontology size {concept_size}")

