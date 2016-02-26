from django import forms
from expensemanager.models import Transaction, Category
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
     help_text="Please enter the category name")

    class Meta:
        model = Category
        fields = ('name',)


class TransactionForm(forms.ModelForm):
    name = forms.CharField(
        max_length=300,
     help_text="Please enter the Transaction Name")
    amount = forms.IntegerField(help_text="Enter Amount")
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    transaction_date = forms.DateInput()
    is_debit = forms.RadioSelect(choices=BOOL_CHOICES)

    class Meta:
        model = Transaction
        exclude = ('userid',)
        widgets = {
            'transaction_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'is_debit': forms.RadioSelect
            }
