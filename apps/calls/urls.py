from django.urls import path
from . import views

app_name = "calls"

urlpatterns = [

    path(
        "incoming/<int:pk>/",
        views.incoming_call,
        name="incoming",
    ),

    path(
        "active/<int:pk>/",
        views.active_call,
        name="active",
    ),

    path(
        "ended/<int:pk>/",
        views.ended_call,
        name="ended",
    ),

    path(
        "api/<int:pk>/",
        views.ai_response,
        name="api_response",
    ),

]
