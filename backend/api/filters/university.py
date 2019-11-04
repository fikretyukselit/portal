from django.db.models import Q
from django_filters import rest_framework as filters

from ..models import University


class UniversityFilterSet(filters.FilterSet):
    city = filters.CharFilter(field_name='city',
                              label='Filter by city.')
    country = filters.CharFilter(field_name='country',
                                 label='Filter by country.')

    def filter_category(self, queryset, name, value):
        bases = University.objects.filter(**{name: value})
        targets = University.objects.filter(**{name: value})
        return queryset.filter(Q(base_equipment__in=bases) | Q(target_equipment__in=targets))
