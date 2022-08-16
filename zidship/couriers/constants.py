# Shipment status
ORDERED = 1
READY_FOR_DELIVERY = 2
DELIVERED = 3
CANCELLED = 4

SHIPMENT_STATUS_TYPES = (
    (ORDERED, 'Ordered'),
    (READY_FOR_DELIVERY, 'Ready for delivery'),
    (DELIVERED, 'Delivered'),
    (CANCELLED, 'Cancelled')
)

# couriers features
CREATE_WAYBILL = 'create_waybill'
PRINT_WAYBILL = 'print_waybill'
TRACKING_SHIPMENT = 'tracking'

FEATURE_ACTIVE_KEY = 'active'
FEATURE_URL_KEY = 'url'
FEATURE_URL_METHOD = 'method'

ALL_FEATURES = [CREATE_WAYBILL, PRINT_WAYBILL, TRACKING_SHIPMENT]

# All methods we need to integrate with couriers 
POST = 'POST'
GET = 'GET'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'

ALL_METHODS = [POST, GET, PUT, PATCH, DELETE]

# Errors 

FEATURE_DOES_NOT_EXIST_ERR = 'Feature does not exist'
FEATURE_IS_CANCELLED = 'Feature is cancelled'
COURIER_RESPONSE_ERR = "Error while calling the courier, please try again later"

# Accepted status code 

ACCEPTED_STATUS_CODE = [200, 201]