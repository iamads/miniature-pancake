from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import Transaction, Category
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("user id"+str(request.user.id))

@login_required
def dashboard(request):
    userid = request.user.id
    transactions = Transaction.objects.filter(userid=userid)
    categories = Category.objects.all()
    return render(request, "expensemanager/dashboard.html",{'transactions':transactions,"categories":categories})

@login_required
def addtransaction(request):
    if request.method == "POST":
        userid = request.user
        name = request.POST['name']
        amount = request.POST['amount']
        category = request.POST['category']
        transaction_date = request.POST['date']
        is_debit = request.POST['is_debit']
        transaction = Transaction.save(userid=userid, name=name , amount=amount, category=category, transaction_date=transaction_date,is_debit=is_debit)
        transaction.save()
        return redirect("/expensemanager/")
    else:
        return render(request, "expensemanager/addtransaction.html")
