import os
from os import environ
import datetime

from Get_Data import get_each_df
from service.file_api import FileAPI
from service.Models.ins_data import INSData

if __name__ == '__main__':
    path = environ.get('PATH_FILES')
    delta = int(environ.get('TIME_DELTA'))
    init_date = environ.get('INIT_DATE')


    #--- se define fecha actual ---#
    final_day = str(datetime.date.today() - datetime.timedelta(days=delta))


    #--- Se crea la lista de regiones ---#
    response, is_invalid = FileAPI.get_regions()
    if is_invalid:
        print("Not regions found")
    else:
        regions = response.get('data')
        for region in regions:
            name = region["name"]         
            file_id = region["hash"]

            path = os.path.join(path,f"{file_id}.parquet")

            nwdf = get_each_df(name,init_date,final_day,path)
            
            nwdf.to_parquet(path,index=False)

            data = INSData(
                file_id="123",
                path=path,
                region=name,
                init_date=init_date,
                final_date=final_day
            )    

            response, is_invalid = FileAPI.insert_data(data)
            if is_invalid:
                print(f"No data insertion for {name}")