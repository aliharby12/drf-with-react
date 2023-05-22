from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import InvoiceFactory, InvoiceGroupFactory
from invoice.models import Invoice
import uuid


class ListAllInvoicesViewTest(APITestCase):
    def setUp(self):
        self.url = reverse("invoice:all-invoices")
        self.invoices = InvoiceFactory.create_batch(size=2)

    def test_list_all_invoices(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class InvoiceDetailsViewTest(APITestCase):
    def setUp(self):
        self.invoice = InvoiceFactory()
        self.url = reverse("invoice:invoice-details",
                           kwargs={"inv_uuid": self.invoice.uuid})

    def test_get_invoice_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invoice_details_not_found(self):
        invalid_uuid = uuid.uuid4()
        url = reverse("invoice:invoice-details",
                      kwargs={"inv_uuid": invalid_uuid})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateInvoiceViewTest(APITestCase):
    def setUp(self):
        self.url = reverse("invoice:create-invoice")
        self.invoice_group = InvoiceGroupFactory.create()

    def test_create_invoice(self):
        data = {
            "description": "Test invoice",
            "group": self.invoice_group.id,
            "item_name": "Test item",
            "price": 9.99,
            "qnty": 1,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)


class UpdateInvoiceViewTest(APITestCase):
    def setUp(self):
        self.invoice = InvoiceFactory()
        self.url = reverse("invoice:update-invoice",
                           kwargs={"inv_uuid": self.invoice.uuid})

    def test_update_invoice(self):
        data = {"description": "Updated invoice description"}
        response = self.client.patch(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.description,
                         "Updated invoice description")

    def test_update_invoice_not_found(self):
        invalid_uuid = uuid.uuid4()
        url = reverse("invoice:update-invoice",
                      kwargs={"inv_uuid": invalid_uuid})
        data = {"description": "Updated invoice description"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DeleteInvoiceViewTest(APITestCase):
    def setUp(self):
        self.invoice = InvoiceFactory()
        self.url = reverse("invoice:delete-invoice",
                           kwargs={"inv_uuid": self.invoice.uuid})

    def test_delete_invoice(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Invoice.objects.filter(
            uuid=self.invoice.uuid).exists())

    def test_delete_invoice_not_found(self):
        invalid_uuid = uuid.uuid4()
        url = reverse("invoice:delete-invoice",
                      kwargs={"inv_uuid": invalid_uuid})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
