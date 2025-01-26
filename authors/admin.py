from django.contrib import admin
from .models import *

@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user','bio','date_of_birth')
    search_fields = ('user__username')
    ordering = ('date_of_birth',)
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'publication_date', 'genre')
    search_fields = ('genre', 'author', 'title',)
    ordering = ('publication_date',)
