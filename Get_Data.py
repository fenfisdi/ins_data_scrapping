import pandas as pd
import numpy as np

from covidcolombia import Report
from covidcolombia import Region

from Models.mongo_collection import Mongo_Colecction
from DB.mongo import MongoEngine
from dotenv import dotenv_values

settings = dotenv_values(".env")
MONGO_URI = settings["MONGO_URI"]
INIT_DATE = settings["INIT_DATE"]

def get_each_df(R_id, D_id, P_id):
    '''
    Función que obtiene las series de tiempo para cada región hasta la fecha dada
    INPUTS: str - Nombre de la región en mayuscúla, str - Fecha en formato yy-mm-dd, path
    OUTPUTS: pandas DataFrame 
    '''
    
    #--- creamos report ---#
    report = Report(P_id, date=D_id, region=R_id, age_range=(0,'MAX_AGE'))
    
    #--- creamos y llenamos el data frame ---#
    dates = pd.date_range(INIT_DATE, D_id)
    deaths = []; recovered = []; infected = []; active_cases = []
    
    for days1 in dates:
        one, two, three = report.get_SIR_populations(day=days1, mode='cummulative')
        deaths.append(one); recovered.append(two); infected.append(three)
        active_cases.append(three-two-one)
        
    all_data = np.transpose(np.array([active_cases, infected, recovered, deaths]))
    df = pd.DataFrame(all_data, columns=['active_cases', 'infected', 'recovered', 'deaths'] )
    df['date'] = dates
    
    return df


def save_all(regions, today, path, function, file_id):
    '''
    función para almacenar las series de tiempo de cada región en una carpeta
    INPUTS: list str - nombres de las regiones en mayuscúla, str - fecha actual, path
    OUTPUT: True
    '''
    mongo = MongoEngine(MONGO_URI)
    mongo.get_connection()

    #--- añadiendo reportes de cada región ---#
    for reg in regions:
        #obtenemos cada dataframe
        nwdf = function(reg, today, path).copy()
         
        collection = Mongo_Colecction()
        collection.File_Id = file_id
        collection.Path = path
        collection.Region = reg
        collection.Update_Date = today
        collection.Init_Date = INIT_DATE
        collection.Final_Date = today        

        collection.save()
        nwdf.to_csv(path, index=False)

    return True