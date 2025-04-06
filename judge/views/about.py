from django.utils.translation import gettext_lazy
from django.views.generic import TemplateView
from judge.utils.views import TitleMixin

class AboutView(TitleMixin, TemplateView):
    template_name = "about.html"
    title = gettext_lazy('About')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_info'] = 'Some additional context if needed'
        return context