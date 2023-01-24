from rest_framework import serializers
from Api.models import Product, Carts, Review
from rest_framework import views
from django.contrib.auth.models import User


class ProductSerializers(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    catagory = serializers.CharField()
    image = serializers.ImageField()


class ProductModelserial(serializers.ModelSerializer):
    avg_rating = serializers.CharField(read_only=True)
    review_count=serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class Userserilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CartSerilizer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    User = serializers.CharField(read_only=True)
    Product = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)

    class Meta:
        model = Carts
        fields = "__all__"


class ReviewSerilizer(serializers.ModelSerializer):
    product = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
