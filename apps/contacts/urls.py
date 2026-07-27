from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path(
        "",
        views.home,
        name="home"
    ),
    path(
        "contact/<int:id>/",
        views.contact_details,
        name="contact_details",
    ),

]
