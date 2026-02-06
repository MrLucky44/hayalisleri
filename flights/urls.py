from django.urls import path
from flights import views

urlpatterns = [
    path("", views.FlightsView.as_view(), name="flights.index"),
]
