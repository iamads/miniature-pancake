from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Transaction, Category, Budget
from forms import CategoryForm, TransactionForm, BudgetForm
# Create your views here.
from datetime import date
from django.core.exceptions import ObjectDoesNotExist

def dashboard(request):
    if request.user.is_authenticated():
        user = request.user
        transactions = Transaction.objects.filter(
            user=user, transaction_date__month=date.today().month)
        try:
            monthlybudget = Budget.objects.get(user=user).monthly
        except ObjectDoesNotExist:
            monthlybudget = 0
        categorical_transactions = {}
        for transaction in transactions:
            category = str(transaction.category)
            if category in categorical_transactions:
                categorical_transactions[category] += transaction.amount
            else:
                categorical_transactions[category] = transaction.amount
        spent_this_month = sum([i.amount for i in transactions])
        return render(
            request, "expensemanager/dashboard.html",
            {'transactions': transactions,
             'monthly_budget': monthlybudget,
             'categorical_transactions': categorical_transactions,
             'spent_this_month': spent_this_month})
    else:
        return redirect("/accounts/login")


@login_required
def addtransaction(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("/expensemanager/")
        else:
            print form.errors
    else:
        form = TransactionForm()
    return render(request, "expensemanager/addtransaction.html",
                  {'categories': categories, 'form': form})


@login_required
def addcategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/expensemanager/")
        else:
            print form.errors

    else:
        form = CategoryForm()
    return render(request, "expensemanager/addcategory.html", {"form": form})


@login_required
def setbudget(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget_form = form.save(commit=False)
            budget_form.user = request.user
            budget_form.save()
            return redirect("/expensemanager/")
        else:
            print form.errors

    else:
        form = BudgetForm()
    return render(request, "expensemanager/setbudget.html", {"form": form})
