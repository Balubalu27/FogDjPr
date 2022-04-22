import math

from .constants import EARTH_RADIUS
from .models import Address


def required_database_objects(answer, radius):
    """ Функция для определения объектов БД по заданным координатам и радиусу """

    geo_latitude = float(answer['geo_lat'])
    geo_longitude = float(answer['geo_lon'])
    coordinate_range = around_coordinates_result(geo_latitude, geo_longitude, radius)
    latitude_max, latitude_min, longitude_max, longitude_min = coordinate_range

    obj_list = Address.objects.filter(
        geo_lat__gte=latitude_min,
        geo_lat__lte=latitude_max,
        geo_lon__gte=longitude_min,
        geo_lon__lte=longitude_max
    )
    return obj_list


def around_coordinates_result(latitude, longitude, radius):
    """
     Функция для расчета диапазона координат.
     На вход подаются координаты (широта и долгота) и радиус (в километрах)
     На выходе получаем диапазон координат, попадающих в заданный радиус.
     """

    delta_lat = compute_delta(latitude)
    delta_lon = compute_delta(longitude)

    around_lat = round(radius / delta_lat, 6)
    around_lon = round(radius / delta_lon, 6)

    coordinate_range_lat = (latitude + around_lat, latitude - around_lat)
    coordinate_range_lon = (longitude + around_lon, longitude - around_lon)

    max_lat = max(coordinate_range_lat)
    min_lat = min(coordinate_range_lat)

    max_lon = max(coordinate_range_lon)
    min_lon = min(coordinate_range_lon)

    return [max_lat, min_lat, max_lon, min_lon]


def compute_delta(degrees):
    return math.pi / 180 * EARTH_RADIUS * math.cos(deg_rad(degrees))


def deg_rad(degrees):
    return degrees * math.pi / 180
