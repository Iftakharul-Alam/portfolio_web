from django.shortcuts import render
from django.views.generic import TemplateView

from resume.models import Resume, Training, Skill


# Create your views here.

class ResumeListView(TemplateView):
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = Resume.objects.all()
        context['training'] = Training.objects.all()
        context['skill'] = Skill.objects.all()
        return context
