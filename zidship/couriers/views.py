from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.decorators import action

from couriers import constants
from .models import Shipment
from .handlers import CourierHandler
from rest_framework.response import Response
from rest_framework import status

from couriers import serializers

class ShipmentViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin):
    serializer_class = serializers.ShipmentSerializer
    queryset = Shipment.objects.all()


    def create(self, request, *args, **kwargs):
        """
            Override create method, need to call Courier API endpoint to create a new shipment
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # need to get the courier object 
        courier_object = serializer.validated_data['courier']

        # check of the courier feature not cancelled
        if not courier_object.features[constants.CREATE_WAYBILL][constants.FEATURE_ACTIVE_KEY]:
            return Response(data={"detail": constants.FEATURE_IS_CANCELLED},status=status.HTTP_400_BAD_REQUEST)

        # Courier handler 
        courier_handler = CourierHandler()

        # call courier API endpoint
        # NOTE: may we need to add headers (API_KEY for example)        
        is_success, data = courier_handler.call_courier_api(
            url=courier_object.features[constants.CREATE_WAYBILL][constants.FEATURE_URL_KEY],
            method=courier_object.features[constants.CREATE_WAYBILL][constants.FEATURE_URL_METHOD],
            data=serializer.validated_data)
        
        if not is_success:
            data = data if data is not None else constants.COURIER_RESPONSE_ERR
            return Response(data={'detail': data}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    

    @action(detail=True, methods=['GET'])
    def tracking(self, request, *args, **kwargs):
        """
            This endpoint responsible for tracking shipments via calling courier API endpoint
        """
        shipment_object = Shipment.objects.filter(tracking_number=self.kwargs['pk']).first()
        courier_object = shipment_object.courier

        # check of the courier feature not cancelled
        if not courier_object.features[constants.TRACKING_SHIPMENT][constants.FEATURE_ACTIVE_KEY]:
            return Response(data={"detail": constants.FEATURE_IS_CANCELLED},status=status.HTTP_400_BAD_REQUEST)
    
        # assuming for now, we need to pass tracking number of shipment as a param
        params = {'tracking_number': shipment_object.tracking_number}

        # Courier handler 
        courier_handler = CourierHandler()
        # call courier API endpoint
        # NOTE: may we need to add headers (API_KEY for example)        
        is_success, data = courier_handler.call_courier_api(
            url=courier_object.features[constants.TRACKING_SHIPMENT][constants.FEATURE_URL_KEY],
            method=courier_object.features[constants.TRACKING_SHIPMENT][constants.FEATURE_URL_METHOD],
            params=params)
        
        if not is_success:
            data = data if data is not None else constants.COURIER_RESPONSE_ERR
            return Response(data={'detail': data}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def waybill(self, request, *args, **kwargs):
        """
            This endpoint responsible for printing or getting waybill of shipments, via calling courier API endpoint
        """
        shipment_object = Shipment.objects.filter(tracking_number=self.kwargs['pk']).first()
        courier_object = shipment_object.courier

        # check of the courier feature not cancelled
        if not courier_object.features[constants.PRINT_WAYBILL][constants.FEATURE_ACTIVE_KEY]:
            return Response(data={"detail": constants.FEATURE_IS_CANCELLED},status=status.HTTP_400_BAD_REQUEST)

        # assuming for now, we need to pass tracking number of shipment as a param
        params = {'tracking_number': shipment_object.tracking_number}

        # Courier handler 
        courier_handler = CourierHandler()
        # call courier API endpoint
        # NOTE: may we need to add headers (API_KEY for example)     
        is_success, data = courier_handler.call_courier_api(
            url=courier_object.features[constants.PRINT_WAYBILL][constants.FEATURE_URL_KEY],
            method=courier_object.features[constants.PRINT_WAYBILL][constants.FEATURE_URL_METHOD],
            params=params)
        
        if not is_success:
            data = data if data is not None else constants.COURIER_RESPONSE_ERR
            return Response(data={'detail': data}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)