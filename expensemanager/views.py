from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Transaction, Category
from forms import CategoryForm, TransactionForm
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("user id"+str(request.user.id))

@login_required
def dashboard(request):
    userid = request.user.id
    transactions = Transaction.objects.filter(userid=userid)
    return render(request, "expensemanager/dashboard.html",{'transactions':transactions})

@login_required
def addtransaction(request):
    if request.method == "POST":
        userid = request.user.id
        name = request.POST['name']
        amount = request.POST['amount']
        category = request.POST['category']
        #transaction_date = request.POST['date']
        is_debit = request.POST['is_debit']
        transaction = Transaction(userid=userid, name=name , amount=amount, category=category, is_debit=is_debit)
        transaction.save()
        return redirect("/expensemanager/")
    else:
        categories = Category.objects.all()
        return render(request, "expensemanager/addtransaction.html", {'categories':categories})

@login_required
def addcategory(request):
    if request.method == "POST":
      # name = request.POST['name']
      # public = request.POST['public']
      # category = Category(name=name, public=public)
      # category.save()
      # return redirect("/expensemanager/")
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/expensemanager/")
        else:
            print form.errors

    else:
        form=CategoryForm()
    return render(request, "expensemanager/addcategory.html",{"form":form})
