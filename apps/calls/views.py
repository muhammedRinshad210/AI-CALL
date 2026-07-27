from django.shortcuts import render, get_object_or_404

from apps.contacts.models import AIContact


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