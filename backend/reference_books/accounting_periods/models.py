# reference_books/models.py

from django.db import models
from ..models import ReferenceBook
from ..agents.models import Agent

class AccountingPeriod(ReferenceBook):
    """
    Справочник AccountingPeriod представляет учетный период, связанный с агентом.
    Предназначен для ведения учета расчета зарплаты сотрудникам в пределах используемого Агентом учетного периода
    В пределах учетного периода ведется фиксация таких показателей как:
    1. количество отработанных часов сотрудниками в разрезе дней
    2. количество опозданий в разрезе дней
    3. количество выдач посылок с пункта выдачи в разрезе дней
    Эти показатели в дальнейшем используются для расчета зарплаты за отработанные часы а так-же стимулирующих выплат в пределах учетного периода
    Атрибуты:
        agent (ForeignKey): Агент, связанный с учетным периодом.
        start_date (DateField): Дата начала учетного периода.
        end_date (DateField): Дата окончания учетного периода.
    """
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Учетный период: {self.start_date} - {self.end_date} ({self.agent})"

    def is_active(self):
        """
        Проверяет, активен ли учетный период на текущую дату.

        Возвращает:
            bool: True, если учетный период активен, иначе False.
        """
        from django.utils import timezone
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date
