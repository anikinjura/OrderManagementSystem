# backend/reference_books/employees/models.py

from django.db import models
from django.contrib.auth.models import User
from ..models import ReferenceBook
from ..agents.models import Agent
from ..pickup_points.models import PickupPoint

class Employee(ReferenceBook):
    """
    Справочник Employee представляет сотрудника, связанного с агентом, и содержит его личную информацию.

    Атрибуты:
        user (OneToOneField): Пользователь, связанный с сотрудником.
        first_name (CharField): Имя сотрудника.
        middle_name (CharField): Отчество сотрудника (необязательно).
        last_name (CharField): Фамилия сотрудника.
        email (EmailField): Уникальный email сотрудника.
        phone_number (CharField): Номер телефона сотрудника (необязательно).
        date_of_birth (DateField): Дата рождения сотрудника.
        date_of_hire (DateField): Дата найма сотрудника.
        position (CharField): Должность сотрудника.
        role (CharField): Роль сотрудника (employee, manager, admin).
        agent (ForeignKey): Агент, с которым связан сотрудник.
        default_pickup_point (ForeignKey): Пункт выдачи по умолчанию (необязательно).
        is_active (BooleanField): Статус активности сотрудника.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_hire = models.DateField()
    position = models.CharField(max_length=100)
    role = models.CharField(
        max_length=50,
        choices=[
            ('employee', 'Employee'),
            ('manager', 'Manager'),
            ('admin', 'Administrator')
        ],
        default='employee'
    )    
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    default_pickup_point = models.ForeignKey(PickupPoint, on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        permissions = [
            ('manage_employees', 'Can manage employees'),
            ('view_personal_data', 'Can view personal data of employees')
        ]

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name} - {self.position}"

    def get_full_name(self):
        """
        Возвращает полное имя сотрудника в формате "Фамилия Имя Отчество".

        Возвращает:
            str: Фамилия Имя Отчество.
        """
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    def deactivate(self):
        """
        Деактивирует сотрудника, устанавливая флаг is_active в False.
        """
        self.is_active = False
        self.save()