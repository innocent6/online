from rest_framework import serializers
from . models import Todo

class Todoserializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        
            )
        
        model = Todo