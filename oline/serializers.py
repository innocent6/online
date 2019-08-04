from rest_framework import serializers
from calc.models import employees


class employeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = ('firstname', 'lastname')
        fields = '__all__'
        


