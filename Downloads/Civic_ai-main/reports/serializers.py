from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)

    class Meta:
        model = Complaint

        fields = '__all__'

        read_only_fields = ['user']