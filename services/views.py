from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    paginate_by = 6
    
    def get_paginate_by(self, queryset):
        # Optionally allow changing page size via URL parameter
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by('-order')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Our Services"
        
        # Add page range for more control in template
        page = context['page_obj']
        context['page_range'] = page.paginator.get_elided_page_range(
            page.number, 
            on_each_side=2,
            on_ends=1
        )
        return context
    
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(Service, slug=slug, is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{self.object.title} | Our Services"
        context['meta_description'] = self.object.description[:160]
        return context