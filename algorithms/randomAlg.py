
#Para cada usuario de test, recomendará puntos de interés aleatorios entre todos los que están en 
#validación y train que el usuario no haya visitado en ninguno de los conjuntos. 

import random

def randomAlgorithm(validationset, trainset, user):
    pois = set()

    # Add POIs from trainset that user has not visited
    with open(trainset) as train:
        for line in train:
            split_line =line.split("\t")
            user_id=split_line[0]
            venue_id =split_line[1]

            if user_id != user:
                pois.add(int(venue_id))

    # Add POIs from validationset that user has not visited
    with open(validationset) as validation:
        for line in validation:
            plit_line =line.split("\t")
            user_id=split_line[0]
            venue_id =split_line[1]

            if user_id != user:
                pois.add(int(venue_id))

    # Convert set to list and shuffle
    pois_list = list(pois)
    random_items = random.sample(pois_list, 30)
    #random.shuffle(pois_list)
    # Return first 40 POIs
    return random_items




