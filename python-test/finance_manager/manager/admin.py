from django.contrib import admin

from manager.models import Budget, Category, Tag, Transaction, Transfer

admin.site.register((Budget, Category, Tag, Transfer, Transaction))
