from rest_framework import serializers
from .models import Report,Methodology

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields="__all__"
    
class MethodologySerializer(serializers.ModelSerializer):
    class Meta:
        model=Methodology
        fields="__all__"