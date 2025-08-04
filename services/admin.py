from django.contrib import admin
from .models import Service
from django.utils.safestring import mark_safe

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'is_active', 'order', 'image_tag', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active', 'order')
    readonly_fields = ('image_tag', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'icon', 'is_active', 'order')
        }),
        ('Media', {
            'fields': ('image', 'image_tag')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_tag(self, obj):
        return obj.image_tag()
    image_tag.short_description = 'Preview'
    
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',)
        }