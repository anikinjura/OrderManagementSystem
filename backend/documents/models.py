# backend/documents/models.py

from django.db import models
from django.conf import settings

class Document(models.Model):
    """
    Базовый класс для всех документов системы.

    Атрибуты:
        document_type (CharField): Тип документа (например, 'Создание', 'Изменение', 'Удаление').
        reference_data (JSONField): Данные, относящиеся к документу.
        user (ForeignKey): Пользователь, который создал или последний раз обновил документ.
        created_at (DateTimeField): Дата и время создания документа.
        updated_at (DateTimeField): Дата и время последнего обновления документа.
        status (CharField): Статус документа (например, 'Черновик', 'На согласовании', 'Утвержден').
    """
    DOCUMENT_TYPES = (
        ('create', 'Создание'),
        ('update', 'Обновление'),
        ('delete', 'Удаление'),
    )

    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('in_review', 'На согласовании'),
        ('approved', 'Утвержден'),
        ('rejected', 'Отклонен'),
    )

    document_type = models.CharField(max_length=10, choices=DOCUMENT_TYPES)
    reference_data = models.JSONField()  # Содержит данные, связанные с документом
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')

    class Meta:
        abstract = True # Это абстрактный класс, он не создаёт таблицу в базе данных

    def __str__(self):
        return f"Document #{self.id} - {self.get_document_type_display()} - {self.get_status_display()}"