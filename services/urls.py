from django.urls import path

from . import views

urlpatterns = [
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='detail'),
]