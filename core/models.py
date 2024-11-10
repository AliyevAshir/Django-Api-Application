from django.db import models

from modeltranslation.translator import translator, TranslationOptions
# Department Model
class Department(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Position Model
class Position(models.Model):
    name = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, related_name='positions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, related_name='employees', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

# Attendance Model
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, related_name='attendance_records', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50)  # e.g., Present, Absent, Leave

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

# Performance Review Model
class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, related_name='performance_reviews', on_delete=models.CASCADE)
    review_date = models.DateField()
    comments = models.TextField()
    rating = models.IntegerField()  # e.g., 1 to 5

    def __str__(self):
        return f"Review for {self.employee.name} on {self.review_date}"

# Training Model
class Training(models.Model):
    employee = models.ForeignKey(Employee, related_name='training_records', on_delete=models.CASCADE)
    training_name = models.CharField(max_length=100)
    date_completed = models.DateField()

    def __str__(self):
        return f"{self.training_name} - {self.employee.name}"

# Compensation Model
class Compensation(models.Model):
    employee = models.ForeignKey(Employee, related_name='compensation_records', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.amount}"

# Document Model
class Document(models.Model):
    employee = models.ForeignKey(Employee, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.employee.name}"

# Message Model
class Message(models.Model):
    sender = models.ForeignKey(Employee, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Employee, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.name} to {self.recipient.name}"

# Onboarding Item Model
class OnboardingItem(models.Model):
    employee = models.ForeignKey(Employee, related_name='onboarding_items', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Onboarding for {self.employee.name} - {self.item}"

# Offboarding Item Model
class OffboardingItem(models.Model):
    employee = models.ForeignKey(Employee, related_name='offboarding_items', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Offboarding for {self.employee.name} - {self.item}"

from django.db import models
from modeltranslation.translator import register, TranslationOptions

