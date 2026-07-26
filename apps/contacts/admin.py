from django.contrib import admin
from .models import AIContact


@admin.register(AIContact)
class AIContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "role",
        "is_online",
        "created_at",
    )

    search_fields = (
        "name",
        "role",
    )

    list_filter = (
        "is_online",
    )