#agrupando por nº veces que usuario ha visitado un lugar. 

cities = ["NewYork_US", "Tokyo_JP"]

for i in cities: 
    file_name = "dataProcessing\\" + i + "Filtered.txt"

    dicc_users = {}
    dicc_ntimes = {}

    with open(file_name) as fileCity:
        for line in fileCity:
            split_line = line.split("\t")
        
            id_user = split_line[0]
            id_lugar = split_line[1]
            
            timestamp = split_line[3].split("\n")[0]
            
            if id_user in dicc_users.keys(): 
            
                dicc_users[id_user][id_lugar] = timestamp
        
            else: 
                dicc_users[id_user] = {id_lugar:timestamp}
            
        
        #DIC FOR Nº TIMES USER VISITED A PLACE: dicc ntimes = userid, poiId : timesvisited 
            key = (id_user, id_lugar)
            
            if key in dicc_ntimes.keys(): 
                dicc_ntimes[key] +=1 
            else:
                dicc_ntimes[key] = 1
                     
    file_name2 = "dataProcessing\\" + i + "Filtered&Grouped.txt"

    
    file = open(file_name2, 'a')

    for key in dicc_ntimes.keys(): 
        user_id = key[0] 
        id_lugar = key[1]
        file.write(str(user_id) + "\t" + str(id_lugar) + "\t" + str(dicc_users[user_id][id_lugar]) + "\t" + str(dicc_ntimes[user_id,id_lugar]) + "\n")

