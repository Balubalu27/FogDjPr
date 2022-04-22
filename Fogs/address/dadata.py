import os

from dadata import Dadata

dadata = Dadata(os.environ.get("TOKEN"), os.environ.get("SECRET"))


def request_use_api(find_address):
    api_answer = dadata.clean("address", find_address)
    return api_answer
