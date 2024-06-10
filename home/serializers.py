from rest_framework import serializers
from .models import Student,Category,Book
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name','age']
        fields='__all__'

    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({"ERROR":"age cant be less than 18"})
        
        if data['name']:
            for char in data['name']:
                if char.isdigit():
                    raise serializers.ValidationError({"error":"Name cannot be numeric"})

        return data
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'