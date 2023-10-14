from django.contrib import admin

from apps.party.models import Warrior, Priest, Mage, Archer


@admin.register(Warrior)
class WarriorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Priest)
class PriestAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Mage)
class MageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Archer)
class ArcherAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]