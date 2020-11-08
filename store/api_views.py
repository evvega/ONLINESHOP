from rest_framework import viewsets
from .serializers import *
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class TutorialViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given contact.
    list:
    Return a list of all the existing contacts.
    create:
    Create a new contact instance.
    update:
    Update an existing contact instance.
    partial_update:
    Update partial an existing contact instance.
    delete:
    Delete  an existing contact instance.
    """
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.all()
    ordering_fields = '__all__'
    filter_class = TutorialFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    search_fields = ('title',)
