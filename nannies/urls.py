from django.urls import path
from . import views

app_name = "nannies"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("add", views.create, name="add"),
    path("<id>", views.show, name="show"),
]
