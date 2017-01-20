from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from .models import Category


class Dropdown(View):
    template_name = 'base.html'

    def get_context_data(self):
        context = {
            'category': Category.objects.all()
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
