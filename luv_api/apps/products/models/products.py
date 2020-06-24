from django.db import models
import uuid
import base64


def make_id():
    return base64.b64encode(uuid.uuid4().bytes).decode("utf-8")


class Product(models.Model):

    id = models.CharField(primary_key=True, max_length=60, unique=True, default=make_id)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    discount_value = models.FloatField(null=True)
    stock = models.IntegerField()

