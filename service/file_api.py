from os import environ
from typing import Union, Tuple

from .response import to_response, UJSONResponse
from .service import API, APIService


class FileAPI:
    api_url = environ.get('FILE_API')
    request = APIService(API(api_url))

    @classmethod
    def get_hash(
        cls,
        region_name: str
        ) -> Tuple[Union[dict, UJSONResponse], bool]:
        parameters = {
            'region': region_name
        }
        response = cls.request.get(f'/scrapping/hash', parameters=parameters)
        if not response.ok:
            return to_response(response), True

        return response.json(), False

    @classmethod
    def get_regions(
        cls,
        region_name: str = None
        ) -> Tuple[Union[dict, UJSONResponse], bool]:

        if region_name is None:\
            parameters = None
        else:
            parameters = {
                'region': region_name
            }

        response = cls.request.get(f'/scrapping/regions', parameters=parameters)
        if not response.ok:
            return to_response(response), False

        return response.json(), True

    @classmethod
    def insert_data(
        cls,
        data: dict
        ) -> Tuple[Union[dict, UJSONResponse], bool]:

        response = cls.request.post(f'/scrapping/Data', data=data)

        if not response.ok:
            return to_response(response), False

        return response.json(), True
