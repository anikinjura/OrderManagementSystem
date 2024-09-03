# backend/registers/changelogs/models.py

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from registers.models import Register

class ChangeLog(Register):
    """
    Лог изменений, осуществляемых документами системы. Наследует базовый класс Register.
    Атрибуты базового класса Register:
        user (ForeignKey): Пользователь, который внёс изменения.
        timestamp (DateTimeField): Время выполнения действия.
    
    Атрибуты:
        document_type (ForeignKey): Тип документа, указывающий на модель, к которой относится запись.
        document_id (PositiveIntegerField): ID документа.
        document (GenericForeignKey): Ссылка на конкретный документ.
        action (CharField): Действие, совершённое пользователем (создание, изменение, удаление).
    """
    document_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    document_id = models.PositiveIntegerField()
    document = GenericForeignKey('document_type', 'document_id')
    action = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Change Log"
        verbose_name_plural = "Change Logs"

    def __str__(self):
        return f"ChangeLog for {self.document_type} #{self.document_id} by {self.user} on {self.timestamp}"
