from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

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
    month_names = [
            "January", "February", "March", "April", 
            "May", "June", "July", "August", 
            "September", "October", "November", "December"
    ]

    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = models.Transaction

    def get_queryset(self):
        month_year = self.request.GET.get("month")
        
        if month_year is not None:
            # convert month string to number
            month = month_year.split(" ")[0]
            for i,m in enumerate(self.month_names):
                if month == m:
                    month = i + 1
                    break

            year = month_year.split(" ")[1]
            transactions = models.Transaction.objects.filter(
                                created_at__year=year,
                                created_at__month=month
                            )
            return transactions

        else:
            month = datetime.datetime.now().month
            year = datetime.datetime.now().year
            transactions = models.Transaction.objects.filter(
                                created_at__year=year,
                                created_at__month=month
                            )
            return transactions

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #get all months in the transaction
        month_year_list = []
        all_transaction = models.Transaction.objects.all()

        for trans in all_transaction:
            # list of month & year
            month_str = self.month_names[trans.created_at.month - 1]
            year_str = trans.created_at.year
            month_year = f"{month_str} {year_str}"
            if month_year not in month_year_list:
                month_year_list.append(month_year)
        
        # calculate credit & debit per months
        total_credit = 0
        total_debit = 0
        current_balance = 0

        transaction_this_month = self.get_queryset()
        
        for trans in transaction_this_month:
            if trans.transaction_type == "Credit":
                total_credit = total_credit + trans.total
            if trans.transaction_type == "Debit":
                total_debit = total_debit + trans.total
            
        current_balance = total_credit - total_debit


        #calculate spendings
        spendings = {}
        spendings["donation"] = 0
        spendings["daily"] = 0
        spendings["holiday"] = 0
        spendings["long"] = 0
        spendings["shopping"] = 0
        spendings["snack"] = 0

        for trans in transaction_this_month:
            if trans.spending == "Donation":
                spendings["donation"] = spendings["donation"] + trans.total
            elif trans.spending == "Daily":
                spendings["daily"] = spendings["daily"] + trans.total
            elif trans.spending == "Holiday":
                    spendings["holiday"] = spendings["holiday"] + trans.total
            elif trans.spending == "Long Term Needs":
                    spendings["long"] = spendings["long"] + trans.total
            elif trans.spending == "Shopping":
                    spendings["shopping"] = spendings["shopping"] + trans.total
            elif trans.spending == "Snack":
                    spendings["snack"] = spendings["snack"] + trans.total


        context["total_credit"] = total_credit
        context["total_debit"] = total_debit
        context["current_balance"] = current_balance
        context["month_year_list"] = month_year_list
        context["spendings"] = spendings
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = models.Transaction
    form_class = forms.TransactionForm
    # template_name = "finance/transaction_form.html"
