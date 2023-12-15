from django.urls import path
from receipts.views import show_receipts

urlpatterns = [
    path("receipts/", show_receipts, name="home"),
]