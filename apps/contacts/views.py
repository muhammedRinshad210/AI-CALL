from django.shortcuts import get_object_or_404, render

from .models import AIContact


def home(request):
    contacts = AIContact.objects.all()

    return render(
        request,
        "contacts/pages/home.html",
        {"contacts": contacts},
    )


def contact_details(request, id):
    contact = get_object_or_404(AIContact, id=id)

    return render(
        request,
        "contacts/pages/details.html",
        {"contact": contact},
    )
