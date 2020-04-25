from django.shortcuts import render

# Create your views here.
import math

from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from parents.models import Parent
from parents.serializers import ParentSerializer
from babies.serializers import BabySerializer
from babies.models import Baby


def get_babies_permission(user, obj, request):
    return user.id == obj.user_id

#Parent View Set para el api/parents
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ParentPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': True,
                    'update': True,
                    'partial_update': True,
                    'get_babies':get_babies_permission,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        parent = serializer.save()
        user = self.request.user
        #assign_perm('parents.view_parent', user, parent)
        #assign_perm('parents.change_parent', user, parent)
        #assign_perm('parents.delete_parent', user, parent)
        
        return Response(serializer.data)



    @action(detail=True, url_path='babies', methods=['get'])
    def get_babies(self, request, pk=None):
        selfParent = self.get_object()
        
        babies = Baby.objects.filter(parent=selfParent)

        if(babies.count()>0):
            return Response(BabySerializer(babies,many=True).data)
        else:
            return Response([])

 