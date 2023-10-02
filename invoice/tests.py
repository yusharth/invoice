# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice_data = {
            'date': '2023-09-30',
            'invoiceCustomerName': 'Test Customer'
        }
        self.invoice = Invoice.objects.create(**self.invoice_data)

        self.detail_data = {
            'invoice': self.invoice,
            'description': 'Product A',
            'quantity': 5,
            'unit_price': '10.00',
            'price': '50.00'
        }
        self.detail = InvoiceDetail.objects.create(**self.detail_data)

    def test_create_invoice(self):
        data = {
            'date': '2023-10-01',
            'invoiceCustomerName': 'New Customer',
            'details': [
                {
                    'description': 'Product B',
                    'quantity': 3,
                    'unit_price': '15.00',
                    'price': '45.00'
                }
            ]
        }

        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)
        self.assertEqual(InvoiceDetail.objects.count(), 2)