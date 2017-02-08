from django.shortcuts import render
from django.views.generic import View
from promo.models import Promo


class Promos(View):
    template_name = 'promo_list/index.html'

    def get_context_data(self):
        context = {
            'promos': Promo.objects.published()
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
