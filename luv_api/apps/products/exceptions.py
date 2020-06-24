from rest_framework.serializers import  ValidationError
from rest_framework import  status

class ProductValidationError(ValidationError):
    default_code = status.HTTP_422_UNPROCESSABLE_ENTITY
