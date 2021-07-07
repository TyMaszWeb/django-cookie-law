from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class AcceptedView(TemplateView):
    template_name = 'accepted.html'
