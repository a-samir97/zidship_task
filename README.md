# Zidship Task 

# System design and Challenges
- Basically, we need to have unified interface for all couriers, we don't need class or interface for every courier. So we need to keep in mind that we should generalize the interface, to be integrated easily with more than 1 couriers

- So what I have done in this challenge, made 2 classes `Shipment` this table or object (ORM) responsible for holding all information about shipments, and another class `Courier` which responsible for holding all information about couriers, this class has 2 fields `name` and `features`.

- let's take about fields in courier model specifically in `features` field, this `JSON Field` contain all information about the feature that we have, so for example assuming we need to create shipment or create waybill for a shipment, we need to know `courier endpoint to call it`, also we need to know abot `method of the request`, and finally `feature is active or cancelled`.

- so features field will look like that 
```
    features={
           "create_waybill": {"url": "http://www.google.com", "active": True, "method": "POST"}, 
           "tracking": {"url": "http://www.google.com", "active": True, "method": "GET"}, 
           "print_waybill": {"url": "http://www.google.com", "active": True, "method": "POST"}
        }
  ```

# How to run the project ?
- create vritual env for the project 
- install all packages and depencies in requirements.txt file 
- finally run `python3 manage.py runserver`

# How to run test ?
- run `python3 manage.py test`

# Documentation and APIs
- run the server by this command `python3 manage.py runserver`
- then go to swagger page, `http://127.0.0.1:8000/swagger/`
- also if you want redoc page, `http://127.0.0.1:8000/redoc/`

# Endpoints 
- `http://127.0.0.1:8000/api/shipments/` -> `POST` to create a new shipment or a new waybill 
- `http://127.0.0.1:8000/api/shipments/1/tracking/` -> `GET` to track shipment 
- `http://127.0.0.1:8000/api/shipments/1/waybill/` -> `GET` to print or get waybill

# Tools
- Python 3
- Django 
- Django Rest Framework 
