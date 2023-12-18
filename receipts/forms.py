from django.forms import ModelForm
from receipts.models import Receipt, Account, ExpenseCategory

class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = (
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        )
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReceiptForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = ExpenseCategory.objects.filter(owner=user)
            self.fields['account'].queryset = Account.objects.filter(owner=user)