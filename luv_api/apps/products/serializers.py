from rest_framework import serializers


from .models import Product
from .exceptions import  ProductValidationError

class ProductSerializer(serializers.ModelSerializer):
    MIN_STOCK = 0
    MIN_VALUE = 1
    MAX_VALUE = 99999.9
    MIN_LENGTH_NAME = 3
    MAX_LENGTH_NAME = 55

    id = serializers.CharField(read_only=True)
    name = serializers.CharField()

    value = serializers.FloatField()

    discount_value = serializers.FloatField(
        required=False

    )

    stock = serializers.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):

        return Product.objects.create(**validated_data)

    def validate_id(self, id):
        if Product.objects.filter(pk=id).exists():
            raise serializers.ValidationError('Id {} already exists'.format(id))

    def validate_name(self, name):
        if (len(name) < self.MIN_LENGTH_NAME) or (len(name) > self.MAX_LENGTH_NAME):
            raise serializers.ValidationError('Invalid product name')
        return name

    def validate_value(self, value):
        if (value <= self.MIN_VALUE) or (value > self.MAX_VALUE):
            return serializers.ValidationError("Invalid value")
        return value

    def validate_stock(self, stock):
        if stock < self.MIN_STOCK:
            raise serializers.ValidationError('Invalid stock value')

        return stock

    def validate(self, attrs):

        discount_value = attrs['discount_value']
        value = attrs['value']
        if not isinstance(value, float):
            raise serializers.ValidationError({"discount_value": 'Value have an error'})

        if isinstance(value, float) and discount_value >= value:
            raise serializers.ValidationError({"discount_value": 'Invalid discount value'})


        return attrs


