from django.urls import path, include
from django.urls import path

from core.views import (
    UserRegisterView,
    UserLoginView,
    LogoutView,
    DepartmentViewSet,
    PositionViewSet,
    EmployeeViewSet,
    AttendanceViewSet,
    PerformanceReviewViewSet,
    TrainingViewSet,
    CompensationViewSet,
    DocumentViewSet,
    MessageViewSet,
    OnboardingItemViewSet,
    OffboardingItemViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance-reviews', PerformanceReviewViewSet)
router.register(r'training', TrainingViewSet)
router.register(r'compensation', CompensationViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'onboarding-items', OnboardingItemViewSet)
router.register(r'offboarding-items', OffboardingItemViewSet)

urlpatterns = [
    path('api/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/logout/', LogoutView.as_view(), name='user-logout'),
    path('api/', include(router.urls)),  # Include core app URLs
]
