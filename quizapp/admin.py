from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from .models import Quiz
from django.db import models

from django.utils.html import format_html
# Register your models here.

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title','quiz_type','slug_link','next_page','total_question','created_at','updated_at']
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    list_filter = ['slug','quiz_type']
    
    # Custom method to make the slug clickable
    def slug_link(self, obj):
        if obj.slug:
            return format_html(f'<a target="_blank" href="/{obj.slug}/"><button type="button" class="button">{obj.slug}</button></a>')
        return '-'
    def next_page(self, obj):
        if obj.next_page_link:
            return format_html(f'<a target="_blank" href="/{obj.next_page_link}/"><button type="button" class="button">{obj.next_page_link}</button></a>')
        return '-'
    def total_question(self, obj):
        if obj.data:
            return len(obj.data)
        return '-'
    slug_link.short_description = 'Slug'

