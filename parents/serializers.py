from rest_framework import serializers

from parents.models import Parent

#Clase Parent Serializer
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'name',
            'id',
            'user_id',
            'user'
        )
