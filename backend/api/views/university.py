from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import University
from ..serializers import UniversitySerializer
from ..filters import UniversityFilterSet
from django_filters.rest_framework import DjangoFilterBackend


class UniversityViewSet(ReadOnlyModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UniversityFilterSet
