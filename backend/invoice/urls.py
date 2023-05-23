from django.urls import path

from typing import *

from invoice.views import *

app_name: str = 'invoice'

urlpatterns: List[path] = [
    path("all-invoices/", ListAllInvoicesView.as_view(), name="all-invoices"),
    path("invoice-detail/<uuid:inv_uuid>/",
         InvoiceDetailsView.as_view(), name="invoice-details"),
    path("create-invoice/", CreateInvoiceView.as_view(), name="create-invoice"),
    path("update-invoice/<uuid:inv_uuid>/",
         UpdateInvoiceView.as_view(), name="update-invoice"),
    path("delete-invoice/<uuid:inv_uuid>/",
         DeleteInvoiceView.as_view(), name="delete-invoice"),
]
