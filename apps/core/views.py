from django.shortcuts import render

from apps.contacts.models import AIContact


def home(request):
    return render(
        request,
        "contacts/pages/home.html",
        {"contacts": AIContact.objects.all()},
    )
