from django.urls import path
from . import views
from .models import Car
from .document import CarDocument


urlpatterns = [
    # path('search/', views.search, name='search'),
]

cars = CarDocument.search().query("match", color="oq")
for car in cars:
    print(car.color)