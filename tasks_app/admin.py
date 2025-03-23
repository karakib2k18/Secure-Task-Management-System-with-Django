from django.contrib import admin
from .models import Task, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'due_date', 'category')
    list_filter = ('status', 'priority', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
