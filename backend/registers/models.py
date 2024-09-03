# backend/registers/models.py

from django.db import models
from django.conf import settings

class Register(models.Model):
    """
    Базовый класс для всех регистров системы.

    Атрибуты:
        user (ForeignKey): Пользователь, который внёс изменения.
        timestamp (DateTimeField): Время выполнения действия.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='action_logs'  # Уникальное имя для обратной связи
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True  # Это абстрактный класс, он не создаёт таблицу в базе данных

    def __str__(self):
        return self.name