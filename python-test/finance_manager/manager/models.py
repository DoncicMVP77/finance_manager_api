from datetime import datetime

from accounts.models import Account
from django.conf import settings
from django.db import models


class Budget(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account')
    name = models.CharField(max_length=150, verbose_name='Name of budget')
    balance = models.DecimalField(max_digits=10, decimal_places=2,
                                  default=0.00, verbose_name='Budget balance')
    date_create = models.DateTimeField(default=datetime.now(), verbose_name='Time of create')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Time of update')

    def __str__(self):
        return self.name


class Category(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE,
                             verbose_name="User")
    name = models.CharField(max_length=225, verbose_name="Category name", unique=True)
    description = models.TextField(verbose_name='Description of category')
    date_create = models.DateTimeField(default=datetime.now(), verbose_name='Time of create')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Time of update')

    def __str__(self):
        return self.name


class Tag(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE,
                                verbose_name='Account')
    name = models.CharField(max_length=125, unique=True, verbose_name="Tag name")
    date_create = models.DateTimeField(default=datetime.now(), verbose_name='Time of create')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Time of update')

    def __str__(self):
        return self.name


class Transfer(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE,
                                     related_name='from_account',
                                     verbose_name="From account")
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE,
                                   related_name='to_account',
                                   verbose_name='To account')
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                default=0.00, verbose_name='Amount money')
    date_create = models.DateTimeField(default=datetime.now(), verbose_name='Time of create')

    def __str__(self):
        return f"{self.from_account} to {self.to_account}"


class Transaction(models.Model):

    Type = (
        ("Income", "Income"),
        ("Expense", "Expense")
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account')
    transaction_type = models.CharField(max_length=75, choices=Type,
                                        verbose_name="Transaction type")
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                default=0.00, verbose_name='Amount money')
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, verbose_name='Budget')
    timestamp = models.DateTimeField(default=datetime.now(), verbose_name='Time of create')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    tag = models.ManyToManyField(Tag)
    description = models.TextField(verbose_name="Description")
    last_update = models.DateTimeField(auto_now=True, verbose_name='Time of update')

    def __str__(self):
        return f"{self.budget}  - {self.category.name} - {self.amount}, {self.timestamp}"
