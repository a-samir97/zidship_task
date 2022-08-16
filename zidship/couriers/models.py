from django.db import models
from . import constants
import requests

class Courier(models.Model):
    """
        This class responsible for holding all couriers informations

        name -> name of the courier (EX - Aramex)
        features -> hold features urls and bool field to check if feature is active or not 
        {
            'create_waybill': {
                'url': 'http:aramex/test/create_waybill/',
                'active': True,
                'method': 'POST'
            }
        }
    """
    name =  models.CharField(max_length=256)
    features = models.JSONField()


class Shipment(models.Model):
    """
        This class responsible for holding all information about shipment
    """
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='shipments')
    weight = models.FloatField()
    status = models.IntegerField(choices=constants.SHIPMENT_STATUS_TYPES, default=constants.ORDERED)
    price = models.FloatField()
    destination = models.CharField(max_length=256)
    tracking_number = models.CharField(max_length=256)
