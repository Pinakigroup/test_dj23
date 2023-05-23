# serializers.py

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    person_phone = serializers.CharField(source='person.phone', read_only=True)
    person_email = serializers.EmailField(source='person.email', read_only=True)
    person_city = serializers.CharField(source='person.city', read_only=True)
    
    class Meta:
        model = Employee
        fields = ['person', 'address', 'designation', 'salary', 'person_phone', 'person_email', 'person_city']
