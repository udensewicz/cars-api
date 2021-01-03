import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .fixtures import seed_test_db, expected_cars_list, expected_popular_cars


def test_post_car(db):
    client = APIClient()
    data = {"make_name": "Toyota", "model_name": "Corolla"}
    response = client.post("/cars/", data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {"id": 1, **data, "average_rate": None}


@pytest.mark.parametrize(
    "input_data, msg",
    [
        ({"make_name": "Toyota", "model_name": "Corolla"}, "The fields make_name, model_name must make a unique set"),
        ({"make_name": "Nonexistent", "model_name": "Nonexistent"}, "Car with provided make/model does not exist!"),
        ({"make_name": "Citroen"}, "This field is required"),
    ],
)
def test_post_car_fail(seed_test_db, input_data, msg):
    client = APIClient()
    response = client.post("/cars/", input_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert msg in str(response.data)


def test_post_rate(seed_test_db):
    client = APIClient()
    data = {"car": 1, "value": 3}
    response = client.post("/rate/", data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {"id": 9, **data}


@pytest.mark.parametrize(
    "input_data, msg",
    [
        ({"car": 1, "value": 10}, '"10" is not a valid choice'),
        (
            {"car": 10, "value": 1},
            'Invalid pk "10" - object does not exist.',
        ),
        (
            {"car": 1},
            "This field is required",
        ),
    ],
)
def test_post_rate_fail(seed_test_db, input_data, msg):
    client = APIClient()
    response = client.post("/rate/", input_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert msg in str(response.data)


def test_get_cars(seed_test_db):
    client = APIClient()
    response = client.get("/cars/", format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_cars_list


def test_get_popular_cars(seed_test_db):
    client = APIClient()
    response = client.get("/popular/", format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_popular_cars
