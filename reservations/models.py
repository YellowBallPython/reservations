from django.db import models


class Reservation(models.Model):
    date = models.DateField(verbose_name='date')
    ci = models.TimeField(verbose_name='check in')
    co = models.TimeField(verbose_name='check out')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.date} / {self.ci}'
