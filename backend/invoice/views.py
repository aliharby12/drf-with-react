from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.throttling import UserRateThrottle
from typing import *

from django.db import transaction
from django.db.models import QuerySet

from invoice.models import Invoice
from invoice.serializer import InvoiceSerializer, AddOrUpdateInvoiceSerializer


class ListAllInvoicesView(ListAPIView):
    serializer_class: Type[InvoiceSerializer] = InvoiceSerializer
    throttle_classes: List[Type[UserRateThrottle]] = [UserRateThrottle]
    filter_backends: List[Type[filters.SearchFilter]] = [filters.SearchFilter]
    search_fields: List[str] = ["description", "group__title", "item_name"]

    def get_queryset(self) -> QuerySet[Invoice]:
        return Invoice.objects.all().order_by("-created_at")


class InvoiceDetailsView(ListAPIView):
    serializer_class: Type[InvoiceSerializer] = InvoiceSerializer

    def get(self, request, inv_uuid, *args, **kwargs) -> Response:
        try:
            inv: Invoice = Invoice.objects.get(uuid=inv_uuid)
            return Response(InvoiceSerializer(inv).data)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateInvoiceView(CreateAPIView):
    serializer_class: Type[AddOrUpdateInvoiceSerializer] = AddOrUpdateInvoiceSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs) -> Response:
        serializer: AddOrUpdateInvoiceSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("created successfully", status=status.HTTP_201_CREATED)


class UpdateInvoiceView(GenericAPIView):
    serializer_class: Type[AddOrUpdateInvoiceSerializer] = AddOrUpdateInvoiceSerializer

    def patch(self, request, inv_uuid) -> Response:
        try:
            inv: Invoice = Invoice.objects.get(uuid=inv_uuid)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer: AddOrUpdateInvoiceSerializer = AddOrUpdateInvoiceSerializer(
            inv, data=request.data, context={"request": request}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("updated successfully", status=status.HTTP_200_OK)


class DeleteInvoiceView(GenericAPIView):
    serializer_class: Type[InvoiceSerializer] = InvoiceSerializer

    def delete(self, request, inv_uuid, format=None) -> Response:
        try:
            inv: Invoice = Invoice.objects.get(uuid=inv_uuid)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        inv.delete()
        return Response("deleted successfully", status=status.HTTP_204_NO_CONTENT)
