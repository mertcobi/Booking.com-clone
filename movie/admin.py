from django.contrib import admin
from .models import *
# Register your models here.

class OtelAdmin(admin.ModelAdmin):
    list_display = ['title','adres','image','rating','map','review_count','price','tax','cancel','room','is_active']
    list_editable = ['is_active']
    search_fields = ['title','adres']
    list_filter = ['title','adres']
    # prepopulated_fields = {'slug':['title']}
    # readonly_fields = ['title']

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','slug']
#     readonly_fields = ['slug']

admin.site.register(Otel,OtelAdmin)
# admin.site.register(category,CategoryAdmin)