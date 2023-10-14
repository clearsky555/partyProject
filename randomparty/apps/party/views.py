from django.shortcuts import render
import names
import random


from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from apps.party.serializers import WarriorSerializer, PriestSerializer, MageSerializer, ArcherSerializer


class CreatePartyView(ListAPIView):
    permission_classes = [AllowAny]

    def get_queryset(self):
        return None

    def get(self, request, *args, **kwargs):
        warrior_data = {'name': names.get_first_name(), 'strength': random.randint(1, 100), 'health': random.randint(1, 100), 'mana': random.randint(1, 100), 'agility': random.randint(1, 100), 'luck': random.randint(1, 100)}
        mage_data = {'name': names.get_first_name(), 'strength': random.randint(1, 100), 'health': random.randint(1, 100), 'mana': random.randint(1, 100), 'agility': random.randint(1, 100), 'luck': random.randint(1, 100)}
        priest_data = {'name': names.get_first_name(), 'strength': random.randint(1, 100), 'health': random.randint(1, 100), 'mana': random.randint(1, 100), 'agility': random.randint(1, 100), 'luck': random.randint(1, 100)}
        archer_data = {'name': names.get_first_name(), 'strength': random.randint(1, 100), 'health': random.randint(1, 100), 'mana': random.randint(1, 100), 'agility': random.randint(1, 100), 'luck': random.randint(1, 100)}

        warrior_serializer = WarriorSerializer(data=warrior_data)
        mage_serializer = MageSerializer(data=mage_data)
        priest_serializer = PriestSerializer(data=priest_data)
        archer_serializer = ArcherSerializer(data=archer_data)

        if (warrior_serializer.is_valid() and mage_serializer.is_valid() and priest_serializer.is_valid() and
                archer_serializer.is_valid()):
            warrior_instance = warrior_serializer.save()
            mage_instance = mage_serializer.save()
            priest_instance = priest_serializer.save()
            archer_instance = archer_serializer.save()

            response_data = {
                "Warrior": WarriorSerializer(warrior_instance).data,
                "Mage": MageSerializer(mage_instance).data,
                "Priest": PriestSerializer(priest_instance).data,
                "Archer": ArcherSerializer(archer_instance).data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Failed to create characters"}, status=status.HTTP_400_BAD_REQUEST)