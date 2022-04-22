import csv
import os

from address.models import Address


def run():
    """ Скрипт для заполнения БД из csv файла """

    strings_list = []
    file_path = os.path.join(os.path.abspath('city.csv'))
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        Address.objects.all().delete()
        for i, row in enumerate(csv_reader):
            one_string = Address(
                id=i+1,
                address=row[0],
                postal_code=row[1],
                country=row[2],
                federal_district=row[3],
                region_type=row[4],
                region=row[5],
                area_type=row[6],
                area=row[7],
                city_type=row[8],
                city=row[9],
                settlement_type=row[10],
                settlement=row[11],
                kladr_id=row[12],
                fias_id=row[13],
                fias_level=row[14],
                capital_marker=row[15],
                okato=row[16],
                oktmo=row[17],
                tax_office=row[18],
                timezone=row[19],
                geo_lat=row[20],
                geo_lon=row[21],
                population=row[22],
                foundation_year=row[23]
            )
            strings_list.append(one_string)

    try:
        Address.objects.bulk_create(strings_list)
        print('Импорт из CSV файла в БД успешно завершен')
    except Exception:
        print('Во время импорта csv файла в БД произошла ошибка')
