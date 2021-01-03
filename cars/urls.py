from django.urls import path
from . import views

urlpatterns = [
    path("cars/", views.CarsList.as_view()),
    path("rate/", views.PostRateView.as_view()),
    path("popular/", views.PopularCarsView.as_view()),
]
