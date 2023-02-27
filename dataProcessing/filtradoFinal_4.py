
cities = ["NewYork_US", "Tokyo_JP"]

for i in cities: 

    dicc_users = {}
    dicc_pois ={}
    dicc_users_aceptados = {}

    file_name = "dataProcessing\\intermediateFiles\\" + i + "Filtered&Grouped.txt"

    with open(file_name) as file: 
        for line_city in file:
            split_line_city = line_city.split("\t")
            
            user_id = split_line_city[0]
            
            poi_id = split_line_city[1]
            
            #user 
            if user_id in dicc_users.keys(): 
                dicc_users[user_id] +=1 
            else:
                dicc_users[user_id] = 1 
            
            #pois
            if poi_id in dicc_pois.keys(): 
                dicc_pois[poi_id] +=1
            else: 
                dicc_pois[poi_id] = 1
    file.close()

    file_name_2 = "dataProcessing\\intermediateFiles\\" + i + "finalVersion.txt"
    file_new = open(file_name_2, 'a')

    with open(file_name) as file:        
    
        for line_city in file:
            split_line_city = line_city.split("\t")
            user_id = split_line_city[0]
            poi_id = split_line_city[1]
            if dicc_users[user_id] >= 5: 
                if dicc_pois[poi_id] >= 5: 
                    file_new.write(line_city)

                    #escribo linea 
            else: 
                pass 
    file.close()