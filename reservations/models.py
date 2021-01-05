from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='date')
    ci = models.TimeField(verbose_name='check in')
    co = models.TimeField(verbose_name='check out')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.date} / {self.ci}'
