from django.shortcuts import render

# Create your views here.
import math

from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from events.models import Event
from events.serializers import EventsSerializer


#Clase EventViewSet para manejar api/events
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_authenticated,
                    'list': False,
                },
                'instance': {
                    'retrieve': 'events.view_event',
                    'destroy': 'events.delete_event',
                    'update': 'events.change_event',
                    'partial_update': 'events.change_event',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        event = serializer.save()
        user = self.request.user
        assign_perm('events.view_event', user, event)
        assign_perm('events.change_event', user, event)
        assign_perm('events.delete_event', user, event)
        return Response(serializer.data)

