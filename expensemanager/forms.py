from django import forms
from expensemanager.models import Transaction, Category, Budget


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
    is_debit = forms.BooleanField(initial=True)

    class Meta:
        model = Transaction
        exclude = ('user',)
        widgets = {
            'transaction_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'is_debit': forms.RadioSelect
            }


class BudgetForm(forms.ModelForm):
    monthly = forms.IntegerField(help_text="Monthly Budget")
    yearly = forms.IntegerField(help_text = "Yearly Budget")

    class Meta:
        model = Budget
        exclude = ('user',)
