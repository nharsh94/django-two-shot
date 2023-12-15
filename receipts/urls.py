from django.urls import path
from receipts.views import show_receipts

urlpatterns = [
    path('', show_receipts, name = 'home'),
    path("receipts/", show_receipts, name="home"),
]