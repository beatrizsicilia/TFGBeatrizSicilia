import math
def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

#Leemos el archivo como lineas, hacemos split pot \t
#Tendremos diccionario así: CodigoPais : [(Ciudad1, lat1, lon1), (Ciudad2, Lat2, Lon2)]
paisciudades ={}
with open("datasets\\foursquare\\dataset_TIST2015_Cities.txt") as fileciudades:

    for line_city in fileciudades:
        split_line_city = line_city.split("\t")
            # 0: nombre ciudad / 1: latitud / 2: Longitud /3: Codigo Pais /4: Nombre /5: tipo 
        pais= str(split_line_city[3])
            
        if pais in paisciudades.keys():
            paisciudades[pais].append((split_line_city[0], split_line_city[1], split_line_city[2]))
        else:
            paisciudades[pais] = [(split_line_city[0], split_line_city[1], split_line_city[2])]


filePOIs_Ciudad = open('dataProcessing\\intermediateFiles\\ficheroPOIsCiudadvf.txt', 'w')  # fichero a escribir
contador = 0

with open("datasets\\foursquare\\dataset_TIST2015_POIs.txt") as ficheropois:
    for line_poi in ficheropois:
        min_dist = 6378  

        split_line_poi = line_poi.split("\t")
        # 0: id foursquare, 1:lat, 2:lon, 3:tipo, 4:Cod pais 

        paises = ("US", "JP")
        
        codpais = split_line_poi[4].strip()
        
        if codpais in paises: 
         
            for key in paisciudades.keys():
                if key == codpais.strip():
                    for cityElement in paisciudades[key]:
                        dist = haversine(float(cityElement[1]), float(cityElement[2]), float(split_line_poi[1]), float(split_line_poi[2]))
                        if dist < min_dist:
                            min_dist = dist
                            #CITY[0] ES EL NOMBRE 
                            ciudad_asignada = cityElement[0]

            # para reducir el tiempo, cremos únicamente el fichero de pois con los pois de las
            # ciudades con las que vamos a trabajar
            if ciudad_asignada == 'New York' or ciudad_asignada == 'Tokyo':
                # incrementamos en 1 el id del poi (mejor q no empiece en 0)
                contador += 1

        
                # escribimos idnuevo + idantiguo + latitud + longitud + ciudad_CountryCode
                filePOIs_Ciudad.write(str(contador) + '\t' + str(split_line_poi[0]) + '\t' + str(split_line_poi[1]) + '\t' + str(split_line_poi[2]) + '\t' + str(split_line_poi[3]) + '\t'+ str(ciudad_asignada.replace(" ", "")) + "_" + str(codpais.strip()) + '\n')
filePOIs_Ciudad.close()



#CHECKINS DATASET 

#diccionario intermedio, almacena keyantiguo: keynuevo, lat, lon 
dicc ={}
with open("dataProcessing\\intermediateFiles\\ficheroPOIsCiudadvf.txt") as fichero:
    for line in fichero:
        split_line = line.split("\t")
        foursquarekey=split_line[1]
        ciudad = split_line[5].replace("\n", "")
        dicc[foursquarekey] = [split_line[0], split_line[2], split_line[3], split_line[4],ciudad]        
fichero.close()        

import os
from datetime import datetime
#venue id, user id, utc time, time offset
with open("datasets\\foursquare\\dataset_TIST2015_Checkins.txt") as ficherocheckins:
    for line_checkin in ficherocheckins:
        split_line_checkin = line_checkin.split("\t")
        idfoursquare = split_line_checkin[1]
        
        if (idfoursquare in dicc.keys()): 
            
            try:
                time_split = split_line_checkin[2].split(" ")
                        #la funcion datetime recibe %d/%b/%Y %H:%M:%S el dataset no viene asi ordenado. 
                        # en dataset Tue Apr 03 18:00:06 +000 2012 (eliminar +000 y colocarlo )
                datetime2 = time_split[2] + '/' + time_split[1] + '/' + time_split[5] + ' ' + time_split[3] 

                time_object= datetime.strptime(datetime2, '%d/%b/%Y %H:%M:%S')

                time = time_object.timestamp()


                idnuevo = dicc[idfoursquare][0]
                    #lat = dicc[idfoursquare][1]
                    #lon = dicc[idfoursquare][2]
                category = dicc[idfoursquare][3]
                ciudad = dicc[idfoursquare][4]

                userid = split_line_checkin[0] 

                fichero = "dataProcessing\\intermediateFiles\\" + ciudad + ".txt"

                if os.path.exists(fichero):
                    with open(fichero, "a") as fcities:
                        fcities.write(str(userid) + '\t' + idnuevo + '\t' + category + '\t' + str(time) + '\n')

                else:
                    with open(fichero, "w") as fcities:
                        fcities.write(str(userid) + '\t' + idnuevo + '\t' + category + '\t' +str(time) + '\n')


            except: 
                pass 
            
            
            
#THE FILES (NY AND TOKIO) DATA WILL FOLLOW: USERID + NEWID + TIMESTAMP             
            
                
        
               

