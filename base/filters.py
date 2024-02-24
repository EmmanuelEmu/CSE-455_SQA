import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *

from django import forms




class StudentFilter(django_filters.FilterSet):
    """
    Filter class for the Student model.

    Inherits from:
    - django_filters.FilterSet: Django's built-in class for creating filters on querysets.

    Attributes:
    - id: Filter for the 'id' field with label 'ID'.
    - name: Case-insensitive filter for the 'name' field with label 'Name'.
    - roll: Filter for the 'roll' field.
    - CGPA_gt: Filter for 'CGPA' field, filtering for values greater than a specified value.
    - status: Filter for the 'status' field with choices provided as a dropdown.


    Django Models:
    - Student: The Django model representing student information.

    Dependencies:
    - Django must be properly installed in the project.
    - django_filters.FilterSet class should be imported from 'django_filters'.
    - Student model should be imported from the appropriate module.


    Notes:
    The filter class provides filters for various fields of the Student model,
    allowing for easy and customizable queryset filtering.

    """
    id = django_filters.NumberFilter(field_name='id', label='ID')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name')
    roll = django_filters.CharFilter(field_name='roll')

    CGPA_gt = django_filters.NumberFilter(field_name='CGPA', lookup_expr='gt', label='CGPA greater than')
    status = CharFilter(field_name='status', lookup_expr='icontains', widget=forms.Select(choices=[('', 'Status')] + list(Student.STATUS)))

    class Meta:
        """
        Metadata class for StudentFilter.

        Attributes:
        - model: The Student model to which the filter is associated.
        - fields: The fields to include in the filter.

        """
        model = Student
        fields = ['id', 'name', 'roll', 'CGPA_gt', 'status']

