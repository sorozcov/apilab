import math

from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from babies.serializers import BabySerializer
from events.serializers import EventsSerializer
from events.models import Event
from parents.models  import Parent

def get_events_permission(user, obj, request):
    
    return user.id == obj.parent.user.pk

#Clase BabyViewSet para consumir api/babies
class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_authenticated,
                    'list': False,
                    
                },
                'instance': {
                    'retrieve': 'babies.view_baby',
                    'destroy': 'babies.delete_baby',
                    'update': 'babies.change_baby',
                    'partial_update': 'babies.change_baby',
                    'get_events': get_events_permission
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.change_baby', user, baby)
        assign_perm('babies.delete_baby', user, baby)
        assign_perm('babies.view_baby', user, baby)
        
        return Response(serializer.data)

    @action(detail=True, url_path='events', methods=['get'])
    def get_events(self, request, pk=None):
        
        selfBaby = self.get_object()
        events = Event.objects.filter(baby=selfBaby.id)
        if(events.count()>0):
            return(Response(EventsSerializer(events,many=True).data))
        else:
            return Response([])
        
        
 

  