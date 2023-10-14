from rest_framework import serializers

from apps.party.models import Warrior, Priest, Archer, Mage


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = '__all__'


class MageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mage
        fields = '__all__'


class PriestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Priest
        fields = '__all__'


class ArcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archer
        fields = '__all__'