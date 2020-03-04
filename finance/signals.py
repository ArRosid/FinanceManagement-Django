from django.db.models import signals
from django.dispatch import receiver

from . import models

@receiver(signals.post_save, sender=models.Credit)
def calculate_balance(sender, instance, *args, **kwargs):
    if instance:
        total_balance = 0

        wallet = instance.wallet

        #all Credit
        all_credit = models.Credit.objects.filter(wallet=wallet)
        for cred in all_credit:
            total_balance = total_balance + cred.total

        #all debit
        all_debit = models.Debit.objects.filter(wallet=wallet)
        for deb in all_debit:
            total_balance = total_balance - deb.total

        wallet_balance = models.Balance.objects.get(wallet=wallet)
        wallet_balance.total = total_balance
        wallet_balance.save()

@receiver(signals.post_save, sender=models.Debit)
def calculate_balance_debit(sender, instance, *args, **kwargs):
    if instance:
        total_balance = 0

        wallet = instance.wallet

        #all Credit
        all_credit = models.Credit.objects.filter(wallet=wallet)
        for cred in all_credit:
            total_balance = total_balance + cred.total

        #all debit
        all_debit = models.Debit.objects.filter(wallet=wallet)
        for deb in all_debit:
            total_balance = total_balance - deb.total

        wallet_balance = models.Balance.objects.get(wallet=wallet)
        wallet_balance.total = total_balance
        wallet_balance.save()
        