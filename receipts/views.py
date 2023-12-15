from django.shortcuts import render
from receipts.models import Receipt


# Create your views here.
def show_receipts(request):
    receipts = Receipt.objects.all()
    context = {
        "receipts": receipts,
    }
    return render(request, "list.html", context)

