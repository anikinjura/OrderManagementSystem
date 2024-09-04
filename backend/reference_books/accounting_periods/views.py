# backend/reference_books/accounting_periods/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import AccountingPeriod

class AccountingPeriodListView(ListView):
    model = AccountingPeriod
    template_name = 'accounting_periods/accounting_period_list.html'

class AccountingPeriodDetailView(DetailView):
    model = AccountingPeriod
    template_name = 'accounting_periods/accounting_period_detail.html'

class AccountingPeriodCreateView(CreateView):
    model = AccountingPeriod
    fields = '__all__'
    template_name = 'accounting_periods/accounting_period_form.html'

class AccountingPeriodUpdateView(UpdateView):
    model = AccountingPeriod
    fields = '__all__'
    template_name = 'accounting_periods/accounting_period_form.html'

class AccountingPeriodDeleteView(DeleteView):
    model = AccountingPeriod
    template_name = 'accounting_periods/accounting_period_confirm_delete.html'
    success_url = '/'
