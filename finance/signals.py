from django.db.models import signals
from django.dispatch import receiver

from . import models

# @receiver(signals.post_save, sender=models.Credit)
# def calculate_balance(sender, instance, *args, **kwargs):
#     if instance:
#         total_balance = 0

#         wallet = instance.wallet

#         #all Credit
#         all_credit = models.Credit.objects.filter(wallet=wallet)
#         for cred in all_credit:
#             total_balance = total_balance + cred.total

#         #all debit
#         all_debit = models.Debit.objects.filter(wallet=wallet)
#         for deb in all_debit:
#             total_balance = total_balance - deb.total

#         wallet_balance = models.Balance.objects.get(wallet=wallet)
#         wallet_balance.total = total_balance
#         wallet_balance.save()

@receiver(signals.post_save, sender=models.Transaction)
def calculate_balance(sender, instance, *args, **kwargs):
    if instance:
        total_balance = 0

        wallet = instance.wallet

        #all transaction
        all_transaction = models.Transaction.objects.filter(wallet=wallet)
        for trans in all_transaction:
            if trans.transaction_type == "Credit":
                total_balance = total_balance + trans.total
            else:
                total_balance = total_balance - trans.total

        wallet_balance = models.Balance.objects.get(wallet=wallet)
        wallet_balance.total = total_balance
        wallet_balance.save()
        