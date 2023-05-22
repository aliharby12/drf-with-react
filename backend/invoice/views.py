from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.throttling import UserRateThrottle

from django.db import transaction

from invoice.models import *
from invoice.serializer import *


class ListAllInvoicesView(ListAPIView):
    serializer_class = InvoiceSerializer
    throttle_classes = [UserRateThrottle]
    filter_backends = [filters.SearchFilter]
    search_fields = ["description", "group__title", "item_name"]

    def get_queryset(self):
        return Invoice.objects.all().order_by("-created_at")
    

class InvoiceDetailsView(ListAPIView):
    serializer_class = InvoiceSerializer

    def get(self, request, inv_uuid, *args, **kwargs):
        try:
            inv = Invoice.objects.get(uuid=inv_uuid)
            return Response(InvoiceSerializer(inv).data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateInvoiceView(CreateAPIView):
    serializer_class = AddOrUpdateInvoiceSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("created successfully", status=status.HTTP_201_CREATED)
    

class UpdateInvoiceView(GenericAPIView):
    serializer_class = AddOrUpdateInvoiceSerializer

    def patch(self, request, inv_uuid):
        try:
            inv = Invoice.objects.get(uuid=inv_uuid)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AddOrUpdateInvoiceSerializer(
            inv, data=request.data, context={"request": request}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("updated successfully", status=status.HTTP_200_OK)


class DeleteInvoiceView(GenericAPIView):
    serializer_class = InvoiceSerializer

    def delete(self, request, inv_uuid, format=None):
        try:
            inv = Invoice.objects.get(uuid=inv_uuid)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        inv.delete()
        return Response("deleted successfully", status=status.HTTP_204_NO_CONTENT)
