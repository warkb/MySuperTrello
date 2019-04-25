from django.views.generic import TemplateView
from .forms import JobForm

class JobFormView(TemplateView):
    template_name = "tutorialAngularDjango/new.html"

    def get_context_data(self, **kwargs):
        context = super(JobFormView, self).get_context_data(**kwargs)
        context.update(JobForm=JobForm())
        return context

class IndexView(TemplateView):
    template_name = 'tutorialAngularDjango/index.html'