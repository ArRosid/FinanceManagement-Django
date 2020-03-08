from django.db import models
from django.urls import reverse

WALLET_CHOICES = (
    ("Mandiri","Mandiri"),
    ("BCA","BCA"),
    ("BRI","BRI"),
    ("Cash","Cash")
)

class Balance(models.Model):
    wallet = models.CharField(max_length=20, choices=WALLET_CHOICES)
    total = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

# class Credit(models.Model):
#     description = models.CharField(max_length=100)
#     total = models.IntegerField()
#     wallet = models.CharField(max_length=20, choices=WALLET_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

class Transaction(models.Model):
    TRANSACTION_CHOICES = (
        ("Credit", "Credit"),
        ("Debit", "Debit")
    )

    SPENDING_CHOICES = (
        ("Donation","Donation"),
        ("Daily", "Daily"),
        ("Holiday", "Holiday"),
        ("Long Term Needs", "Long Term Needs"),
        ("Shopping", "Shopping"),
        ("Snack", "Snack")
    )

    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES)
    wallet = models.CharField(max_length=20, choices=WALLET_CHOICES)
    total = models.IntegerField()
    description = models.CharField(max_length=255)
    spending = models.CharField(max_length=100, choices=SPENDING_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('transaction_list')