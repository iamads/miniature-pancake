from django import forms
from expensemanager.models import Transaction, Category


class CategoryForm(forms.ModelForm):
    name= forms.CharField(max_length = 50, help_text="Please enter the category name")
    public = forms.CheckboxInput()


    class Meta:
        model=Category
        fields = ('name','public')


class TransactionForm(forms.ModelForm):
    name = forms.CharField(max_length=300, help_text="Please enter the Transaction Name")
    amount = forms.IntegerField(help_text="Enter Amount")
    category = forms.CharField(max_length=50, help_text="Enter Category")
    is_debit = forms.CheckboxInput()


    class Meta:
        model = Transaction
        fields = ('name','amount','category','is_debit')
