import requests
from django.db.models import Count
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from . import models, serializers

CARS_API_URL = "https://vpic.nhtsa.dot.gov/api/"


class CarsList(generics.ListCreateAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarListSerializer

    def perform_create(self, serializer):
        requested_make = serializer.validated_data.get("make_name")
        requested_model = serializer.validated_data.get("model_name")

        # the make filter checks against a LIKE condition, so the exact match needs to be checked later
        make_models = requests.get(
            "{}/vehicles/GetModelsForMake/{}?format=json".format(CARS_API_URL, requested_make)
        ).json()["Results"]

        # make comparison is case insensitive because the api returns the names as all uppercase
        if not any(
            item["Model_Name"] == requested_model and item["Make_Name"].lower() == requested_make.lower()
            for item in make_models
        ):
            raise ValidationError("Car with provided make/model does not exist!")

        serializer.save()


class PostRateView(generics.CreateAPIView):
    queryset = models.Rate.objects.all()
    serializer_class = serializers.RateSerializer


class PopularCarsView(generics.ListAPIView):
    queryset = models.Car.objects.all().annotate(num_rates=Count("rate")).order_by("-num_rates")
    serializer_class = serializers.CarPopularSerializer
