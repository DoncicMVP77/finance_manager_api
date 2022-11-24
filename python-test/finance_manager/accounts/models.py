from datetime import datetime

from django.db import models
from django.conf import settings


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                verbose_name='UserAccount')
    balance = models.DecimalField(max_digits=10, decimal_places=2,
                                  default=0.00, verbose_name='Account balance')
    date_create = models.DateTimeField(default=datetime.now(), verbose_name='Time of create')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Time of update')

    def __str__(self):
        return self.user.email
