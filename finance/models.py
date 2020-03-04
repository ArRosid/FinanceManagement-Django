from django.db import models

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

class Credit(models.Model):
    description = models.CharField(max_length=100)
    total = models.IntegerField()
    wallet = models.CharField(max_length=20, choices=WALLET_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

class Debit(models.Model):
    TYPE_CHOICES = (
        ("Donation","Donation"),
        ("Daily", "Daily"),
        ("Holiday", "Holiday"),
    )
    wallet = models.CharField(max_length=20, choices=WALLET_CHOICES)
    total = models.IntegerField()
    description = models.CharField(max_length=255)
    type_spending = models.CharField(max_length=100, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)