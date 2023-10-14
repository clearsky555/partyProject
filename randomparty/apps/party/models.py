from django.db import models


class Warrior(models.Model):
    name = models.CharField("имя", max_length=100)
    strength = models.IntegerField("сила")
    health = models.IntegerField("здоровье")
    mana = models.IntegerField("мана")
    agility = models.IntegerField("ловкость")
    luck = models.IntegerField("удача")

    class Meta:
        verbose_name = "Воин"
        verbose_name_plural = "Воины"

    def __str__(self):
        return f"{self.name}"


class Mage(models.Model):
    name = models.CharField("имя", max_length=100)
    strength = models.IntegerField("сила")
    health = models.IntegerField("здоровье")
    mana = models.IntegerField("мана")
    agility = models.IntegerField("ловкость")
    luck = models.IntegerField("удача")

    class Meta:
        verbose_name = "Маг"
        verbose_name_plural = "Маги"

    def __str__(self):
        return f"{self.name}"


class Priest(models.Model):
    name = models.CharField("имя", max_length=100)
    strength = models.IntegerField("сила")
    health = models.IntegerField("здоровье")
    mana = models.IntegerField("мана")
    agility = models.IntegerField("ловкость")
    luck = models.IntegerField("удача")

    class Meta:
        verbose_name = "Жрец"
        verbose_name_plural = "Жрецы"

    def __str__(self):
        return f"{self.name}"


class Archer(models.Model):
    name = models.CharField("имя", max_length=100)
    strength = models.IntegerField("сила")
    health = models.IntegerField("здоровье")
    mana = models.IntegerField("мана")
    agility = models.IntegerField("ловкость")
    luck = models.IntegerField("удача")

    class Meta:
        verbose_name = "Лучник"
        verbose_name_plural = "Лучники"

    def __str__(self):
        return f"{self.name}"