from django.db import models


class AIContact(models.Model):

    name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    avatar = models.URLField()

    description = models.TextField()

    is_online = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name