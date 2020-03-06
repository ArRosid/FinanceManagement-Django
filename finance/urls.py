from django.urls import path
from . import views

urlpatterns = [
    path("", views.BalanceList.as_view(), 
             name="balance"),

    path("transactions", views.TransactionListView.as_view(),
                        name="transaction_list"),

    path("transactions/create", views.TransactionCreateView.as_view(),
                        name="transaction_create"),


]