import statistics
from rest_framework import serializers
from . import models


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = "__all__"


class CarListSerializer(CarSerializer):
    average_rate = serializers.SerializerMethodField()

    def get_average_rate(self, obj):
        rates = obj.rate_set.values_list("value", flat=True)
        return statistics.mean(rates) if len(rates) else None


class CarPopularSerializer(CarSerializer):
    num_rates = serializers.SerializerMethodField()

    def get_num_rates(self, obj):
        return obj.rate_set.count()


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rate
        fields = "__all__"
