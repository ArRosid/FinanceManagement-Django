from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from . import models

class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ('transaction_type', 'wallet', 'total',
                  'description', 'spending')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))