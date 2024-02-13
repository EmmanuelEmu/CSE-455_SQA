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
    id = django_filters.NumberFilter(field_name='id',label='ID')
    name = django_filters.CharFilter(lookup_expr='icontains',label='Name')
    reg_no = django_filters.CharFilter(lookup_expr='icontains',label='Reg No')
    rank = django_filters.ChoiceFilter(choices=Teacher.RANK,label='Rank')
    dept = django_filters.ModelChoiceFilter(queryset=Department.objects.all(),label='Department')

    class Meta:
        model = Teacher
        fields = ['name', 'reg_no', 'rank', 'dept']