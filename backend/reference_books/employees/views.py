# backend/reference_books/employees/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/employee_form.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/employee_form.html'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = '/'
