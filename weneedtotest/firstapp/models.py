from django.contrib.auth.models import User
from django.db import models


class TemporaryPassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    temporary_password = models.CharField(max_length=12)
    created_at = models.DateTimeField()


class Media(models.Model):
    name = models.CharField(max_length=10, verbose_name='name')
    image = models.ImageField(upload_to='images/')

    class Meta:
        unique_together = ['name']
        verbose_name = 'Media'

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
