from django.urls import path
from receipts.views import show_receipts, create_receipt

urlpatterns = [
    path("", show_receipts, name="home"),
    path("create/", create_receipt, name="create_receipt")
]