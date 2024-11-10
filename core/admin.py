from django.contrib import admin
from .models import (
    Department,
    Position,
    Employee,
    Attendance,
    PerformanceReview,
    Training,
    Compensation,
    Document,
    Message,
    OnboardingItem,
    OffboardingItem,
)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'department', 'created_at', 'updated_at')
    search_fields = ('name', 'department__name')
    list_filter = ('department', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'department', 'position', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'surname', 'email', 'department__name', 'position__name')
    list_filter = ('department', 'position', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    # Inline modeller eklemek için
    class DocumentInline(admin.TabularInline):
        model = Document
        extra = 1

    inlines = [DocumentInline]  # Document modelini ekleyin

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    search_fields = ('employee__name', 'date')
    list_filter = ('status', 'date')

class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('employee', 'review_date', 'rating')
    search_fields = ('employee__name', 'comments')
    list_filter = ('review_date', 'rating')

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('employee', 'training_name', 'date_completed')
    search_fields = ('employee__name', 'training_name')
    list_filter = ('date_completed',)

class CompensationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'date')
    search_fields = ('employee__name', 'amount')
    list_filter = ('date',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'file', 'upload_date')
    search_fields = ('employee__name',)
    list_filter = ('upload_date',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp')
    search_fields = ('sender__name', 'recipient__name', 'content')
    list_filter = ('timestamp',)

class OnboardingItemAdmin(admin.ModelAdmin):
    list_display = ('employee', 'item', 'completed')
    search_fields = ('employee__name', 'item')
    list_filter = ('completed',)

class OffboardingItemAdmin(admin.ModelAdmin):
    list_display = ('employee', 'item', 'completed')
    search_fields = ('employee__name', 'item')
    list_filter = ('completed',)
from modeltranslation.translator import register, TranslationOptions
from .models import Employee

from modeltranslation.translator import translator, TranslationOptions
from .models import Department, Position, Employee

class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'created_at', 'updated_at')  # Include created_at and updated_at
    required_languages = ('en', 'az')
    fallback_language = 'en'

    # Define the field translations for Azerbaijani
    translations = {
        'name': 'departament',
        'created_at': 'yaratma_tarixi',
        'updated_at': 'güncəllənmə_tarixi',
    }

class PositionTranslationOptions(TranslationOptions):
    fields = ('name', 'created_at', 'updated_at')  # Include created_at and updated_at
    required_languages = ('en', 'az')
    fallback_language = 'en'

    # Define the field translations for Azerbaijani
    translations = {
        'name': 'pozisiya',
        'created_at': 'yaratma_tarixi',
        'updated_at': 'güncəllənmə_tarixi',
    }
from modeltranslation.translator import translator, TranslationOptions
from .models import Employee

class EmployeeTranslationOptions(TranslationOptions):
    fields = ('name', 'surname')  # Include fields to be translated
    required_languages = ('en', 'az')  # Specify the required languages
    fallback_language = 'en'  # Set fallback language

    # Define the translations for Azerbaijani
    translations = {
        'name': 'ad',
        'surname': 'soyad'
        
        
    }

# Register the translation options
translator.register(Employee, EmployeeTranslationOptions)





# Register the translation options
translator.register(Department, DepartmentTranslationOptions)
translator.register(Position, PositionTranslationOptions)

# Ensure Employee is registered only once
if not translator._registry.get(Employee):
    translator.register(Employee)


# Modelleri admin paneline kaydetme
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(PerformanceReview, PerformanceReviewAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Compensation, CompensationAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(OnboardingItem, OnboardingItemAdmin)
admin.site.register(OffboardingItem, OffboardingItemAdmin)
