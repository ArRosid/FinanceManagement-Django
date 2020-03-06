from django.contrib import admin

from . import models

class BalanceAdmin(admin.ModelAdmin):
    list_display = ["wallet", "total"]
    list_filter = ["total",]

# class CreditAdmin(admin.ModelAdmin):
#     list_display = ["description", "total", "wallet", "created_at"]
#     list_filter = ["total", "wallet", "created_at"]

class TransactionAdmin(admin.ModelAdmin):
    list_display = ["transaction_type", "wallet", "total",
                    "spending", "created_at"]
    list_filter = ["transaction_type", "wallet",
                    "total", "created_at"]

admin.site.register(models.Balance, BalanceAdmin)
admin.site.register(models.Transaction, TransactionAdmin)


