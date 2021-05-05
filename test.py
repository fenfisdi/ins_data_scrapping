import os

import datetime

from dotenv import dotenv_values
from Get_Data import save_all, get_each_df

settings = dotenv_values(".env")
INS_DATA = settings["INS_DATA"]

#--- se define la ruta --#


#--- se define fecha actual ---#
today = str(datetime.date.today())


#--- Se crea la lista de regiones ---#
to_report = ['Colombia', 'BOGOTA', 'VALLE', 'ANTIOQUIA', 'MEDELLIN', 'CALI', 'BELLO',
             'ITAGUI', 'ENVIGADO', 'SABANETA', 'CALDAS', 'COPACABANA', 'LA ESTRELLA',
             'BARBOSA', 'GIRARDOTA']


folder_all = str('reporte_' + today)
file_id = "2"

path = os.path.join(os.getcwd(),INS_DATA,f"{file_id}.csv") #insdata


save_all(to_report, today, path, get_each_df, file_id )