import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from .models import *

from django import forms



class DepartmentFilter(django_filters.FilterSet):
    id = NumberFilter(field_name='id')
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Dept Name')
    location = CharFilter(field_name='location', lookup_expr='icontains', widget=forms.Select(choices=[('', 'All Blocks')] + list(Department.LOCATION)))
    rank = NumberFilter(field_name='rank')
    phone = CharFilter(field_name='phone',lookup_expr='icontains')
    email = CharFilter(field_name='email',lookup_expr='icontains')

    class Meta:
        model = Department
        fields = ['id', 'name', 'location', 'rank', 'phone', 'email']
        exclude = ['date_created', 'description']



class TeacherFilter(django_filters.FilterSet):
    """
    FilterSet for filtering instances of the Teacher model.

    This FilterSet provides filters for querying instances of the Teacher model
    based on various fields such as ID, name, registration number, rank, and department.

    Example usage:

    .. code-block:: python

        # Create a filter instance
        filter = TeacherFilter(request.GET, queryset=Teacher.objects.all())

        # Apply filters
        filtered_teachers = filter.qs

    For more information on working with Django Filter, see:
    https://django-filter.readthedocs.io/en/stable/

    """
    id = django_filters.NumberFilter(field_name='id',label='ID')
    """
    Filter for filtering by ID.

    :param int id: The ID to filter by.
    """
    name = django_filters.CharFilter(lookup_expr='icontains',label='Name')
    """
    Filter for filtering by name.

    :param str name: The name to filter by.
    """
    reg_no = django_filters.CharFilter(lookup_expr='icontains',label='Reg No')
    """
    Filter for filtering by registration number.

    :param str reg_no: The registration number to filter by.
    """
    rank = django_filters.ChoiceFilter(choices=Teacher.RANK,label='Rank')
    """
    Filter for filtering by rank.

    :param str rank: The rank to filter by.
    """
    dept = django_filters.ModelChoiceFilter(queryset=Department.objects.all(),label='Department')
    """
    Filter for filtering by department.

    :param Department dept: The department to filter by.
    """

    class Meta:
        model = Teacher
        fields = ['name', 'reg_no', 'rank', 'dept']