from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.exceptions import TokenError
from core.serializers import (
    DepartmentSerializer, PositionSerializer, EmployeeSerializer,
    LoginSerializer, LoginSerializer, AttendanceSerializer,
    PerformanceReviewSerializer, TrainingSerializer,UserRegisterSerializer,
    CompensationSerializer, DocumentSerializer, MessageSerializer,
    OnboardingItemSerializer, OffboardingItemSerializer
)
from .models import (
    Department, Position, Employee,
    Attendance, PerformanceReview, Training,
    Compensation, Document, Message,
    OnboardingItem, OffboardingItem
)

# Base Model ViewSet
class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Require authentication for all actions

# User Registration View
# User Registration View
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        name = self.request.data.get('name')
        password = self.request.data.get('password')
        serializer.save(username=name, password=password)

# User Login View
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# User Login View
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from .serializers import UserLoginSerializer  # Ensure this is the correct import
from .models import Employee  # Ensure this is the correct import
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from .serializers import UserLoginSerializer  # Ensure this is the correct import
from .models import Employee  # Ensure this is the correct import

class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @extend_schema(
        request=UserLoginSerializer,
        responses={
            200: {
                'description': 'Login successful',
                'examples': [
                    {
                        'value': {
                            "message": "Login successful",
                            "token": "your_access_token",
                            "refresh": "your_refresh_token"
                        }
                    }
                ]
            },
            400: {
                'description': 'Invalid credentials',
                'examples': [
                    {
                        'value': {
                            "non_field_errors": ["Unable to log in with provided credentials."]
                        }
                    }
                ]
            }
        }
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)  # Generate the JWT tokens
            return Response({
                "message": "Login successful",
                "token": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Deletion View
class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def delete(self, request, user_id):
        if not request.user.is_superuser:
            return Response({"message": "Admin access required."}, status=status.HTTP_403_FORBIDDEN)
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# Logout View
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can log out

    def post(self, request):
        try:
            token = request.data.get('refresh')
            if not token:
                return Response({'detail': 'Token is required.'}, status=status.HTTP_400_BAD_REQUEST)

            OutstandingToken.objects.get(token=token).blacklist()
            return Response({'success': 'You have been logged out successfully.'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'detail': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)

# Department ViewSet
class DepartmentViewSet(BaseModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"message": "Admin access required."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

# Position ViewSet
class PositionViewSet(BaseModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"message": "Admin access required."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

# Employee ViewSet
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer, EmployeeAZSerializer  # New serializer for Azerbaijani

from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer, EmployeeAZSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    
    def get_serializer_class(self):
        """
        Select serializer based on URL language context.
        """
        # Use Azerbaijani serializer if the request path contains '/az'
        if '/az' in self.request.path:
            return EmployeeAZSerializer
        # Default to English serializer
        return EmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Restrict deletion to superusers only.
        """
        if not request.user.is_superuser:
            return Response({"message": "Admin access required."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

# Attendance ViewSet
class AttendanceViewSet(BaseModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"message": "Admin access required."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

# Performance Review ViewSet
class PerformanceReviewViewSet(BaseModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

# Training ViewSet
class TrainingViewSet(BaseModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

# Compensation ViewSet
class CompensationViewSet(BaseModelViewSet):
    queryset = Compensation.objects.all()
    serializer_class = CompensationSerializer

# Document ViewSet
class DocumentViewSet(BaseModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# Message ViewSet
class MessageViewSet(BaseModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# Onboarding Item ViewSet
class OnboardingItemViewSet(BaseModelViewSet):
    queryset = OnboardingItem.objects.all()
    serializer_class = OnboardingItemSerializer
    

# Offboarding Item ViewSet
class OffboardingItemViewSet(BaseModelViewSet):
    queryset = OffboardingItem.objects.all()
    serializer_class = OffboardingItemSerializer



# core/views.py
# core/views.py

from django.shortcuts import render
from .tasks import send_email_task

# core/views.py

from django.shortcuts import render
from .tasks import send_email_task

def some_view(request):
    # After some action, send an email
    subject = 'Welcome to Our Service'
    message = 'Thank you for signing up! We are glad to have you.'
    send_email_task.delay(subject, message, ['asuraliyev405@gmail.com'])
    return render(request, 'email.html')
