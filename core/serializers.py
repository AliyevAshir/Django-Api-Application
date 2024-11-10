from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import (
    Department, Position, Employee,
    Attendance, PerformanceReview, Training,
    Compensation, Document, Message,
    OnboardingItem, OffboardingItem  
)

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['name', 'password']

    def create(self, validated_data):
        user = User(username=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        return data

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

from rest_framework import serializers
from .models import Employee



from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Employee  # Ensure this is the correct import

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Employee  # Ensure this is the correct import

class UserLoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        name = data.get('name')
        password = data.get('password')

        if name and password:
            user = authenticate(username=name, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Must include 'name' and 'password'.")

        return data
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'created_at', 'updated_at']  # Model sahə adları

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name', 'salary', 'department', 'created_at', 'updated_at']  # Model sahə adları

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'email', 'department', 'position', 'status', 'created_at', 'updated_at']  # Model sahə adları
class EmployeeAZSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'email', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'label': 'Ad'},
            'surname': {'label': 'Soyad'},
            'email': {'label': 'E-poçt'},
            'created_at': {'label': 'Yaratma Tarixi'},
            'updated_at': {'label': 'Güncəllənmə Tarixi'},
        }
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'date', 'status']  # Model sahə adları

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = ['id', 'employee', 'review_date', 'comments', 'rating']  # Model sahə adları

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id', 'employee', 'training_name', 'date_completed']  # Model sahə adları

class CompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compensation
        fields = ['id', 'employee', 'amount', 'date']  # Model sahə adları

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'employee', 'file', 'upload_date']  # Model sahə adları

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp']  # Model sahə adları

class OnboardingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingItem
        fields = ['id', 'employee', 'item', 'completed']  # Model sahə adları

class OffboardingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffboardingItem
        fields = ['id', 'employee', 'item', 'completed']  # Model sahə adları

# core/serializers.py
from rest_framework import serializers


