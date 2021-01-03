from django.db import models


class Car(models.Model):
    make_name = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)

    class Meta:
        unique_together = ["make_name", "model_name"]


class Rate(models.Model):
    CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    value = models.PositiveSmallIntegerField(choices=CHOICES)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
