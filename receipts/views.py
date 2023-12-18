from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import CreateExpenseCategoryForm, ReceiptForm, CreateAccountForm


# Create your views here.
@login_required
def show_receipts(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)

@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST, user=request.user)

        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create_recipe.html", context)

@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "receipts/categories/category_list.html", context)

@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts,
    }
    return render(request, "receipts/accounts/accounts_list.html", context)

@login_required
def create_category(request):
    if request.method == "POST":
        form = CreateExpenseCategoryForm(request.POST)

        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    
    else:
        form = CreateExpenseCategoryForm()

    context = {"form": form}
    return render(request, "receipts/categories/create_category.html", context)

@login_required
def create_account(request):
    if request.method == "POST":
        form = CreateAccountForm(request.POST)

        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect("accounts_list")

    else:
        form = CreateAccountForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/accounts/create_account.html", context)