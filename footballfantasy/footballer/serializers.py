from rest_framework import serializers

from .models import Club, Footballer


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class FootballerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = "__all__"
