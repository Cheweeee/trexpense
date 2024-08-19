from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date')

admin.site.register(Expense, ExpenseAdmin)