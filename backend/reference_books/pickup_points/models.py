from django.db import models
from ..models import ReferenceBook
from ..agents.models import Agent

class PickupPoint(ReferenceBook):
    """
    Справочник PickupPoint представляет пункт выдачи, связанный с агентом.

    Атрибуты:
        address (CharField): Адрес пункта выдачи.
        agent (ForeignKey): Связь с моделью Agent.
    """
    address = models.CharField(max_length=255)
    agent = models.ForeignKey(Agent, related_name='pickup_points', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
