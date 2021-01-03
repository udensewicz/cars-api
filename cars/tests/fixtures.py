import pytest
from ..models import Car, Rate


@pytest.fixture
def seed_test_db(db):
    honda = Car.objects.create(make_name="Honda", model_name="Trail 125")
    merc = Car.objects.create(make_name="Mercedes-Benz", model_name="420")
    toyota = Car.objects.create(make_name="Toyota", model_name="Corolla")

    for rate in [4, 3, 2, 4]:
        Rate.objects.create(value=rate, car=toyota)
    for rate in [3, 5, 5]:
        Rate.objects.create(value=rate, car=honda)
    Rate.objects.create(value=5, car=merc)


expected_popular_cars = [
    {"id": 3, "num_rates": 4, "make_name": "Toyota", "model_name": "Corolla"},
    {"id": 1, "num_rates": 3, "make_name": "Honda", "model_name": "Trail 125"},
    {"id": 2, "num_rates": 1, "make_name": "Mercedes-Benz", "model_name": "420"},
]

expected_cars_list = [
    {"id": 1, "average_rate": 4.333333333333333, "make_name": "Honda", "model_name": "Trail 125"},
    {"id": 2, "average_rate": 5, "make_name": "Mercedes-Benz", "model_name": "420"},
    {"id": 3, "average_rate": 3.25, "make_name": "Toyota", "model_name": "Corolla"},
]
