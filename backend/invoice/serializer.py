from rest_framework import serializers

from invoice.models import Invoice, InvoiceGroup


class InvoiceGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceGroup
        exclude = ('id', 'created_at', 'updated_at')
        read_only_fields = ('uuid',)


class InvoiceSerializer(serializers.ModelSerializer):
    group = InvoiceGroupSerializer(read_only=True)

    class Meta:
        model = Invoice
        exclude = ('id', 'updated_at')
        read_only_fields = ('uuid', 'invoice_number', 'group')


class AddOrUpdateInvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ('description', 'item_name', 'price', 'qnty', 'group')
