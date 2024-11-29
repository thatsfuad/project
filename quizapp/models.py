from django.db import models
from datetime import datetime
from django.utils.text import slugify

QUIZ_TYPE = [
    ('blue', 'Blue'),
    ('blue_extra', 'Blue Extra'),
    ('blue_yellow', 'Blue Yellow'),
    ('blue_yellow_extra', 'Blue Yellow Extra'),        
]

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    quiz_type = models.CharField(choices=QUIZ_TYPE, max_length=20)
    next_page_link = models.CharField(max_length=255, blank=True, null=True)
    data = models.JSONField(default=list, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            base_slug = slugify(self.title)
            custom_slug = base_slug.replace('-', '_')
            self.slug = custom_slug
        super().save(*args, **kwargs)

