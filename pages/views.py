from django.views.generic import TemplateView
from appointment.models import Service, StaffMember
from django.urls import reverse

class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all services (no is_active filter since field doesn't exist)
        services = Service.objects.all().order_by('name')[:3]
        
        # Add staff members and appointment URLs to each service
        for service in services:
            # Get staff members offering this service
            service.staff_members = StaffMember.objects.filter(services_offered=service)
            # Generate appointment URL
            service.appointment_url = reverse('appointment:appointment_request', kwargs={'service_id': service.id})
        
        context['services'] = services
        context['total_services'] = Service.objects.count()  # Removed is_active filter
        return context

class AboutView(TemplateView):
    template_name = 'pages/about.html'
