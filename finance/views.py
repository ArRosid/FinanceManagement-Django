from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms

class BalanceList(LoginRequiredMixin, ListView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = models.Balance

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        total = 0
    
    
        balances = models.Balance.objects.all()
        for balance in balances:
            total = total + balance.total

        context["total"] = total
        return context

class TransactionListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = models.Transaction

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        total_credit = 0
        total_debit = 0
        current_balance = 0

        all_transaction = models.Transaction.objects.all()

        for trans in all_transaction:
            if trans.transaction_type == "Credit":
                total_credit = total_credit + trans.total
            if trans.transaction_type == "Debit":
                total_debit = total_debit + trans.total
            
        current_balance = total_credit - total_debit

        context["total_credit"] = total_credit
        context["total_debit"] = total_debit
        context["current_balance"] = current_balance
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = models.Transaction
    form_class = forms.TransactionForm
    # template_name = "finance/transaction_form.html"
