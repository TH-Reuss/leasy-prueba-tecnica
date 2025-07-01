from django.views.generic import ListView
from django.utils.http import urlencode
from django.db.models import Q

class CustomListView(ListView):
    available_columns = {}  # { 'Label': 'campo' }
    default_columns = []    # ['campo', ...]
    paginate_by = 20

    def get_queryset(self):
        columns_param = self.request.GET.get('columns')
        selected_attrs = columns_param.split(',') if columns_param else self.default_columns
        queryset = self.model.objects.values(*selected_attrs)

        search_query = self.request.GET.get('search')
        if search_query:
            filters = Q()
            for attr in selected_attrs:
                if '__' not in attr:
                    filters |= Q(**{f"{attr}__icontains": search_query})
            queryset = queryset.filter(filters)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        valid_attr_values = set(self.available_columns.values())

        columns_param = self.request.GET.get('columns')
        if columns_param:
            selected_values = [
                val for val in columns_param.split(',') if val in valid_attr_values
            ]
        else:
            selected_values = self.default_columns

        selected_columns = {
            label: value for label, value in self.available_columns.items()
            if value in selected_values
        }

        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        

        context.update({
            'available_columns': self.available_columns,
            'selected_columns': selected_columns,
            'query_string': urlencode(query_params, doseq=True),
        })
        return context
