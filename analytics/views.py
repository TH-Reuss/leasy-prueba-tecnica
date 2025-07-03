import datetime
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Q
from contracts.models import Contract, Invoice
from clients.models import Client
from cars.models import Car, CarModel
import calendar
from dateutil.relativedelta import relativedelta

class IndexView(LoginRequiredMixin, View):

    def _get_month_range(self, date):
        """Retorna el primer y último día del mes dado."""
        start = date.replace(day=1)
        last_day = calendar.monthrange(date.year, date.month)[1]
        end = date.replace(day=last_day)
        return start, end
    
    def _get_upcoming_revenue_chart(self):
        current_date = datetime.date.today()
        chart_labels = []
        chart_data = []

        for i in range(12):
            month_date = current_date + relativedelta(months=i)
            month_start, month_end = self._get_month_range(month_date)

            total = Invoice.objects.filter(
                due_date__range=(month_start, month_end),
                contract__is_active=True
            ).aggregate(total=Sum('amount'))['total'] or 0

            chart_labels.append(calendar.month_abbr[month_date.month])
            chart_data.append(float(total))

        return chart_labels, chart_data


    def get(self, request):
        contracts_count = Contract.objects.count()
        clients_count = Client.objects.count()
        cars_count = Car.objects.count()
        car_models_count = CarModel.objects.count()

        cars_with_contracts_ids = Contract.objects.filter(
            is_active=True,
            deleted_at__isnull=True
        ).values_list('car_id', flat=True).distinct()

        total_cars_with_contracts = Car.objects.filter(id__in=cars_with_contracts_ids).count()
        total_cars_without_contracts = Car.objects.exclude(id__in=cars_with_contracts_ids).count()

        revenue_chart_labels, revenue_chart_data = self._get_upcoming_revenue_chart()
        recent_contracts = Contract.objects.select_related('client', 'car__model__brand').order_by('-created_at')[:20]
        print(recent_contracts)
        context = {
            'contracts_count': contracts_count,
            'clients_count': clients_count,
            'cars_count': cars_count,
            'car_models_count': car_models_count,
            'total_cars_with_contracts': total_cars_with_contracts,
            'total_cars_without_contracts': total_cars_without_contracts,
            'revenue_chart_labels': revenue_chart_labels,
            'revenue_chart_data': revenue_chart_data,
            'recent_contracts': recent_contracts,
        }
        return render(request, 'analytics/index.html', context)
