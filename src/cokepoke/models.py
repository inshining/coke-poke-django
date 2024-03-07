import string

from django.db import models
from django.utils import timezone

class Currency(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    code = models.CharField(max_length=3, null=False, blank=False, unique=True)
    symbol = models.CharField(max_length=5, null=False, blank=False, default='$')

    def __str__(self) -> str:
        return self.code

class Transaction(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    currency = models.ForeignKey(Currency, null=False, blank=False, default=1, on_delete=models.PROTECT)
    message = models.TextField(null=True, blank=True)

    @property
    def link(self):
        return f"localhost/payment/{str(self.id)}"

