from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Transaction, Category
from forms import CategoryForm, TransactionForm
# Create your views here.
from django.http import HttpResponse
from datetime import date


def dashboard(request):
    if request.user.is_authenticated():
        userid = request.user.id
        transactions = Transaction.objects.filter(userid=userid,transaction_date__month=date.today().month)
        spent_this_month = sum([i.amount for i in transactions])
        return render(request, "expensemanager/dashboard.html",{'transactions':transactions,'spent_this_month':spent_this_month})
    else:
        return redirect("/accounts/login")


@login_required
def addtransaction(request):
    categories = Category.objects.all()
    if request.method == "POST":
       form = TransactionForm(request.POST)
       if form.is_valid():
           transaction = form.save(commit=False)
           transaction.userid = request.user.id
           transaction.save()
           return redirect("/expensemanager/")
       else:
           print form.errors
    else:
        form = TransactionForm()
    return render(request, "expensemanager/addtransaction.html", {'categories':categories,'form':form})


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
        form=CategoryForm()
    return render(request, "expensemanager/addcategory.html",{"form":form})
