from django.views.generic import TemplateView
from django.db.models import Count
from services.models import Service

class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get 3 active services ordered by priority
        context['services'] = Service.objects.filter(is_active=True).order_by('-order')[:3]
        # Get total active services count
        context['total_services'] = Service.objects.filter(is_active=True).count()
        return context
