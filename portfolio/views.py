from django.shortcuts import render
from django.views.generic import TemplateView

from portfolio.models import Portfolio, Category


# Create your views here.


class PortfolioListView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['portfolio'] = Portfolio.objects.all()
        return context
