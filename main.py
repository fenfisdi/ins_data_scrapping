import datetime
import os

from Get_Data import get_each_df
from service.Models.ins_data import INSData
from service.file_api import FileAPI


if __name__ == '__main__':
    file_path = os.environ.get('FILE_PATH')
    delta = int(os.environ.get('TIME_DELTA'))

    # dates
    init_date = os.environ.get('INIT_DATE')
    final_date = str(datetime.date.today() - datetime.timedelta(days=delta))

    response, is_valid = FileAPI.get_regions()
    regions = response.get('data')

    if is_valid or len(regions) > 0:
        for region in regions:
            name = region['name']
            file_id = region['hash']

            new_df = get_each_df(name, init_date, final_date, path)
            path = os.path.join(path, f"{file_id}.parquet")

            new_df.to_parquet(path, index=False)
            data = INSData(
                    file_id = str(final_date),
                    path = path,
                    region = name,
                    init_date = init_date,
                    final_date = final_date
                    )

            response, is_invalid = FileAPI.insert_data(data)
            if is_invalid:
                print(f'No new data added for {name}')
