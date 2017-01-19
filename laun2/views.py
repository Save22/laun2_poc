from django.shortcuts import render

from django.views.generic import View

from .models import Promo, SlideImage
# Create your views here.

class Index(View):
    template_name = 'new.html'

    def get_context_data(self):
        context = {
            'context': Promo.objects.all(),
            'slide': SlideImage.objects.all(),
        }
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
