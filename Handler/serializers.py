from rest_framework import serializers
from . models import Login_info,SignUp_info,Cart_info,Products,Admin,Contact

class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login_info
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp_info
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_info
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'