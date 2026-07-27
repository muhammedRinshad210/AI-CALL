from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from apps.contacts.models import AIContact

from .services import get_ai_response


def incoming_call(request, pk):

    contact = get_object_or_404(
        AIContact,
        pk=pk
    )

    return render(
        request,
        "calls/pages/incoming.html",
        {
            "contact": contact
        }
    )


def active_call(request, pk):

    contact = get_object_or_404(
        AIContact,
        pk=pk
    )

    return render(
        request,
        "calls/pages/active.html",
        {
            "contact": contact
        }
    )


def ended_call(request, pk):

    contact = get_object_or_404(
        AIContact,
        pk=pk
    )

    return render(
        request,
        "calls/pages/ended.html",
        {
            "contact": contact
        }
    )


def ai_response(request, pk):
    get_object_or_404(AIContact, pk=pk)

    return JsonResponse({"message": get_ai_response()})
