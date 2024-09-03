# backend/reference_books/models.py

from django.db import models

class ReferenceBook(models.Model):
    """
    Базовый класс для всех справочников системы. Содержит общие поля и методы.
    
    Атрибуты:
        name (CharField): Название справочника.
        description (TextField): Описание справочника (необязательное).
        created_at (DateTimeField): Дата и время создания справочника.
        updated_at (DateTimeField): Дата и время последнего обновления справочника.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Это абстрактный класс, он не создаёт таблицу в базе данных

    def __str__(self):
        return self.name
