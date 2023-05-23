from rest_framework import serializers

from invoice.models import Invoice, InvoiceGroup

from typing import *


class InvoiceGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model: Type[InvoiceGroup] = InvoiceGroup
        exclude: Tuple[str, ...] = ('id', 'created_at', 'updated_at')
        read_only_fields: Tuple[str, ...] = ('uuid',)


class InvoiceSerializer(serializers.ModelSerializer):
    group: InvoiceGroupSerializer = InvoiceGroupSerializer(read_only=True)

    class Meta:
        model: Type[Invoice] = Invoice
        exclude: Tuple[str, ...] = ('id', 'updated_at')
        read_only_fields: Tuple[str, ...] = ('uuid', 'invoice_number', 'group')


class AddOrUpdateInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model: Type[Invoice] = Invoice
        fields: Tuple[str, ...] = ('description', 'item_name', 'price', 'qnty', 'group')
