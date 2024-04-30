from django.urls import path
from . import views
from .views import NewView, IndexView

app_name = "nannies"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("new", NewView.as_view(), name="new"),
    path("add", views.create, name="add"),
    path("<id>/edit", views.edit, name="edit"),
    path("<id>/delete", views.delete, name="delete"),
    path("<id>", views.show, name="show"),
]
