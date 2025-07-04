from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task) 
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created_at')
    list_filter = ('completed','created_at',)
    search_fields = ('title',)
       