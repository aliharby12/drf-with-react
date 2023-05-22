from django.db import models

import uuid
import random


class TimeStampedModel(models.Model):
    """
    database model for created at and updated at fields
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False, unique=True)

    class Meta:
        abstract = True


class InvoiceGroup(TimeStampedModel):
    """
    database model for invoice groups
    """
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Invoice(TimeStampedModel):
    invoice_number = models.PositiveIntegerField(
        max_length=10, unique=True, editable=False)
    description = models.TextField()
    group = models.ForeignKey(InvoiceGroup, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    qnty = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()
        super().save(*args, **kwargs)

    def generate_invoice_number(self):
        return random.randint(100000000, 999999999)

    def __str__(self) -> str:
        return str(self.invoice_number)
