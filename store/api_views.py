from rest_framework import viewsets
from .models import *
from .serializers import *


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
