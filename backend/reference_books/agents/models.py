# backend/reference_books/agents/models.py

from django.db import models
from ..models import ReferenceBook

class Agent(ReferenceBook):
    """
    Справочник Agent представляет агента - влыдельца пунктов выдачи

    Атрибуты:
        email (EmailField): Уникальный email агента.
        phone_number (CharField): Уникальный номер телефона агента.
    """
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def get_pickup_points(self):
        """
        Возвращает все пункты выдачи, связанные с агентом.

        Возвращает:
            QuerySet: Набор пунктов выдачи, связанных с агентом.
        """
        return self.pickup_points.all()
    
    def __str__(self):
        return self.name