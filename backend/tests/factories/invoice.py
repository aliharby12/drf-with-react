import random, factory

from factory.django import DjangoModelFactory

from invoice.models import InvoiceGroup, Invoice


class InvoiceGroupFactory(DjangoModelFactory):
    class Meta:
        model = InvoiceGroup

    title = factory.Faker("word")


class InvoiceFactory(DjangoModelFactory):
    class Meta:
        model = Invoice

    invoice_number = factory.Sequence(lambda n: n)
    description = factory.Faker("paragraph")
    group = factory.SubFactory(InvoiceGroupFactory)
    item_name = factory.Faker("word")
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    qnty = factory.Faker("random_int", min=1, max=10)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        Override the default _create method to set the invoice number
        """
        invoice = super()._create(model_class, *args, **kwargs)
        invoice.invoice_number = invoice.generate_invoice_number()
        invoice.save()
        return invoice
