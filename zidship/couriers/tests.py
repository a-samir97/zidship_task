from django.test import TestCase
from rest_framework import status
from unittest import mock
from . import models, constants
from model_bakery import baker

class TestShipmentsAPIs(TestCase):

    def setUp(self) -> None:
        
        self.__set_up_objects__()

        self.create_shipment_url = '/api/shipments/'
        self.print_waybill_url = '/api/shipments/{tracking_number}/waybill/'
        self.tracking_shipments_url = '/api/shipments/{tracking_number}/tracking/'

    def __set_up_objects__(self):
        self.courier = models.Courier.objects.create(
            name='Aramex',
            features={
                "create_waybill": {"url": "http://www.google.com", "active": True, "method": "POST"}, 
                "tracking": {"url": "http://www.google.com", "active": True, "method": "GET"}, 
                "print_waybill": {"url": "http://www.google.com", "active": True, "method": "POST"}}
        )
        self.shipment = baker.make(models.Shipment, courier=self.courier)


    def tearDown(self) -> None:
        models.Shipment.objects.all().delete()
        models.Courier.objects.all().delete()
    
    @mock.patch('couriers.handlers.CourierHandler.call_courier_api')
    def test_create_shipment_success_case(self, mock_request):
        mock_request.return_value = (True, {"testData": 'correctData'})
        data = {
            "weight": 0,
            "status": 1,
            "price": 0,
            "destination": "string",
            "tracking_number": "123123123",
            "courier": self.courier.id
        }

        response = self.client.post(self.create_shipment_url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data)

    @mock.patch('couriers.handlers.CourierHandler.call_courier_api')
    def test_create_shipment_failure_case(self, mock_request):
        mock_request.return_value = (False, {"testData": 'correctData'})
        data = {
            "weight": 0,
            "status": 1,
            "price": 0,
            "destination": "string",
            "tracking_number": "123123123",
            "courier": self.courier.id
        }

        response = self.client.post(self.create_shipment_url, data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(response.data)
    
    @mock.patch('couriers.handlers.CourierHandler.call_courier_api')
    def test_track_shipment_success_case(self, mock_request):
        mock_request.return_value = (True, {'status': 'Ordered'})
        response = self.client.get(self.tracking_shipments_url.format(tracking_number=self.shipment.tracking_number))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    @mock.patch('couriers.handlers.CourierHandler.call_courier_api')
    def test_track_shipment_failure_case(self, mock_request):
        mock_request.return_value = (False, {'error': 'there is an error'})
        response = self.client.get(self.tracking_shipments_url.format(tracking_number=self.shipment.tracking_number))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(response.data)
    
    @mock.patch('couriers.handlers.CourierHandler.call_courier_api')
    def test_print_waybill_success_case(self, mock_request):
        mock_request.return_value = (True, {'status': 'Ordered'})
        response = self.client.get(self.print_waybill_url.format(tracking_number=self.shipment.tracking_number))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    @mock.patch('couriers.handlers.CourierHandler.call_courier_api')
    def test_print_waybill_failure_case(self, mock_request):
        mock_request.return_value = (False, {'error': 'there is an error'})
        response = self.client.get(self.print_waybill_url.format(tracking_number=self.shipment.tracking_number))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(response.data)
    
