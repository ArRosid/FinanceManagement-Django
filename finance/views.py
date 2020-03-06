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


class TransactionCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = models.Transaction
    form_class = forms.TransactionForm
    # template_name = "finance/transaction_form.html"
