from django import forms
from expensemanager.models import Transaction, Category
categories = Category.objects.all()
category_choices = tuple([(i,i) for i in categories])
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
     help_text="Please enter the category name")
    public = forms.CheckboxInput()

    class Meta:
        model = Category
        fields = ('name', 'public')


class TransactionForm(forms.ModelForm):
    name = forms.CharField(
        max_length=300,
     help_text="Please enter the Transaction Name")
    amount = forms.IntegerField(help_text="Enter Amount")
    category = forms.ChoiceField(widget=forms.Select, choices=category_choices)
    transaction_date = forms.DateInput()
    is_debit = forms.RadioSelect(choices=BOOL_CHOICES)

    class Meta:
        model = Transaction
        exclude = ('userid',)
        widgets = {
            'transaction_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'is_debit': forms.RadioSelect
            }
