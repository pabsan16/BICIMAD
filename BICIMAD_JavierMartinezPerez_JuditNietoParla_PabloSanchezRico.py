

"""
PRÁCTICA: BICIMAD

AUTORES: JAVIER MARTINEZ PEREZ, JUDIT NIETO PARLA, PABLO SANCHEZ RICO
"""

from random import random

from pyspark import SparkContext, SparkConf

import json

"""
Creamos los grupos (estaciones y año completo).
"""



winter2019=['Datos_2019/diciembre.json', 'Datos_2019/enero.json', 'Datos_2019/febrero.json']
spring2019=['Datos_2019/marzo.json', 'Datos_2019/abril.json', 'Datos_2019/mayo.json']
summer2019=['Datos_2019/junio.json', 'Datos_2019/julio.json', 'Datos_2019/agosto.json']
autumn2019=['Datos_2019/septiembre.json', 'Datos_2019/octubre.json', 'Datos_2019/noviembre.json']



winter2020=['Datos_2020/diciembre.json', 'Datos_2020/enero.json', 'Datos_2020/febrero.json']
spring2020=['Datos_2020/marzo.json', 'Datos_2020/abril.json', 'Datos_2020/mayo.json']
summer2020=['Datos_2020/junio.json', 'Datos_2020/julio.json', 'Datos_2020/agosto.json']
autumn2020=['Datos_2020/septiembre.json', 'Datos_2020/octubre.json', 'Datos_2020/noviembre.json']


with SparkContext() as sc:
        
    def union(group):
        """
        Unimos los datos de los ficheros que pertenecen a la 
        misma estación (o si estamos estudiando el año entero,
        todos los meses del año).
        """
        rddlist=[]
        for month in group:
            rddlist.append(sc.textFile(month))
        rdd=sc.union(rddlist)
        return rdd
    
    def datos(line):
        """
        Nos quedamos únicamente con los datos que nos interesan 
        de los que aparecen en los ficheros (por ejemplo, la 
        estación en la que se inicia el viaje y en la que se 
        termina).
        """
        data=json.loads(line)
        usertype=data['user_type']
        userdaycode=data['user_day_code']
        start=data['idunplug_station']
        end=data['idplug_station']
        return usertype, userdaycode, start, end
    
    def sort(rdd):
        """
        Ordenamos las estaciones en orden creciente en cuanto al 
        número de bicis que acaban teniendo.
        """
        rdd=rdd.map(datos)
        selected_type=1
        rdd_users=rdd.filter(lambda x: x[0]==selected_type).map(lambda x: x[1:])
        rdd_users_salida=rdd_users.map(lambda x: (x[1],x[2]))
        rdd_users_entrada=rdd_users.map(lambda x: (x[2],x[1]))
        rdd_entrada=rdd_users_entrada.groupByKey().mapValues(list).mapValues(len)
        rdd_salida=rdd_users_salida.groupByKey().mapValues(list).mapValues(len).map(lambda x: (x[0],-x[1]))
        lista=[rdd_entrada, rdd_salida]
        rdd_total=sc.union(lista)
        rdd_total=rdd_total.groupByKey().mapValues(list).map(lambda x: (x[0],sum(x[1])))
        rdd_ord=rdd_total.sortBy(lambda x:x[1])
        return rdd_ord
    
    
    """
    Mostramos por pantalla las listas de las estaciones 
    (organizadas en estaciones y año completo) ya ordenadas.
    """
    
    #2019
    print("--------------------------- 2019 ------------------------------")
    
    rdd_winter2019=sort(union(winter2019))
    winter_list2019=rdd_winter2019.collect()
    print("---------------------------WINTER-----------------------------")
    print(winter_list2019)
    
    
    rdd_spring2019=sort(union(spring2019))
    spring_list2019=rdd_spring2019.collect()
    print("---------------------------SPRING-----------------------------")
    print(spring_list2019)
    
    
    rdd_summer2019=sort(union(summer2019))
    summer_list2019=rdd_summer2019.collect()
    print("---------------------------SUMMER-----------------------------")
    print(summer_list2019)
    
    
    rdd_autumn2019=sort(union(autumn2019))
    autumn_list2019=rdd_summer2019.collect()
    print("---------------------------AUTUMN-----------------------------")
    print(autumn_list2019)
    
    
    
    """
    Mostramos por pantalla las listas de las estaciones 
    (organizadas en estaciones y año completo) ya ordenadas.
    """
    
    #2020
    print("--------------------------- 2020 ------------------------------")
    
    rdd_winter2020=sort(union(winter2020))
    winter_list2020=rdd_winter2020.collect()
    print("---------------------------WINTER-----------------------------")
    print(winter_list2020)
    
    
    rdd_spring2020=sort(union(spring2020))
    spring_list2020=rdd_spring2020.collect()
    print("---------------------------SPRING-----------------------------")
    print(spring_list2020)
    
    
    rdd_summer2020=sort(union(summer2020))
    summer_list2020=rdd_summer2020.collect()
    print("---------------------------SUMMER-----------------------------")
    print(summer_list2020)
    
    
    rdd_autumn2020=sort(union(autumn2020))
    autumn_list2020=rdd_summer2020.collect()
    print("---------------------------AUTUMN-----------------------------")
    print(autumn_list2020)
    
    
    
    sc.stop() #es necesario cerrar el Spark context