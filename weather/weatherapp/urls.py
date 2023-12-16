from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="homepage"),
    path("/delete/<str:city_name>/", views.delete_city, name="delete_city"),
]
