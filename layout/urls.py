from django.urls import path
from layout import views


urlpatterns = [
    path("", views.index, name="home"),
]
