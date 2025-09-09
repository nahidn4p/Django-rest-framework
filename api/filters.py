import django_filters
from employees.models import Employees



class EmployeeFilter(django_filters.FilterSet):
        designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
        name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
        id = django_filters.RangeFilter(field_name='id')
        class Meta:
                model=Employees
                fields=['designation','name','id']
        