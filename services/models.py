from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.text import slugify

def service_image_upload_path(instance, filename):
    return f'services/service_{instance.id}/{filename}'

class Service(models.Model):
    title = models.CharField(_('Service Name'), 
                             max_length=100,
                             validators=[MinLengthValidator],
                             help_text='Service title (5-100 characters)'
                            )
    slug = models.SlugField(max_length=120, unique=True, blank=True,
                          help_text='URL-friendly version of the title (auto-generated)')
    description = models.TextField(
        max_length=1000,
        validators=[MinLengthValidator(20)],
        help_text='Detailed service description (20-1000 characters)'
    )
    icon = models.CharField(
        max_length=50,
        default='fas fa-user-md',
        help_text='Font Awesome icon class'
    )
    image = models.ImageField(
        upload_to=service_image_upload_path,
        help_text='Service card image (recommended size: 600x400px)'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='whether the service should be displayed'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(
        default=0,
        help_text='Ordering field (higher numbers come first)'
    )

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-order', '-created_at']
        indexes = [
            models.Index(fields=['is_active']),
            models.Index(fields=['order']),
            models.Index(fields=['slug']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Handle potential duplicates
            original_slug = self.slug
            counter = 1
            while Service.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
    
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="150" height="100" />')
        return "No Image"
    image_tag.short_description = 'Image Preview'

    def get_related_services(self, limit=3):
        """
        Returns related services (excluding current one)
        Ordered by the same criteria as the main list
        """
        return Service.objects.filter(
            is_active=True
        ).exclude(
            pk=self.pk
        ).order_by(
            '-order', '-created_at'
        )[:limit]
