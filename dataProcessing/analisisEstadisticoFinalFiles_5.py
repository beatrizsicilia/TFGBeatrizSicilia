import pandas as pd

cities = ["NewYork_US", "Tokyo_JP"]
dataTotal = []

for i in cities: 
    file_name = "dataProcessing\\intermediateFiles\\" + i + "finalVersion.txt"
    dicc_users = {}
    dicc_venueid = {}
    dicc_reps = {}
    numero_checkins = 0

    with open(file_name) as fichero: 
        for line in fichero:
            line_split = line.split("\t")
            numero_checkins +=1 
            user_id = line_split[0]
            id_venue = line_split[1]
            
            if user_id in dicc_users.keys(): 
                dicc_users[user_id] +=1
            else: 
                dicc_users[user_id] = 1 
            
            if id_venue in dicc_venueid.keys(): 
                dicc_venueid[id_venue] +=1
            else: 
                dicc_venueid[id_venue] = 1
                
                
            #REPETIDOS: 
            timestampn= line_split[2]
            time = timestampn.split("\n")[0]
            
            if (user_id,id_venue) not in dicc_reps.keys(): 
                dicc_reps[(user_id,id_venue)] = time 

    unique_users = len(dicc_users)
    unique_POIs = len(dicc_venueid)
    mean_checkinsuser = round(sum(dicc_users.values()) / unique_users , 2)

    #AGRUPAMOS EN DATOS
    data = {"Ciudad":  [i], "Nºusuarios":  [unique_users], "Nºcheckis": [numero_checkins], "NºPOIs": [unique_POIs], "Avg checkins/usuario": [mean_checkinsuser]}

    dataTotal.append(data)



tablainfo1 = pd.DataFrame(dataTotal[0])
tablainfo2 = pd.DataFrame(dataTotal[1])
df = pd.concat([tablainfo1, tablainfo2])
print(df)





