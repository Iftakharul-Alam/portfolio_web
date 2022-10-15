from django.shortcuts import render
from django.views.generic import TemplateView

from me.models import About, PersonalInfo, Language, IELTS, GRE, PersonalSkill, Education, JOBS


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.last()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.last()
        context['p_info'] = PersonalInfo.objects.all()
        context['language'] = Language.objects.all()
        context['ielts'] = IELTS.objects.all()
        context['gre'] = GRE.objects.all()
        context['skill'] = PersonalSkill.objects.all()
        context['education'] = Education.objects.all()
        context['jobs'] = JOBS.objects.all()
        return context
