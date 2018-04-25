# Django Imports:
from django.contrib import admin
from django.contrib.auth.models import User, Group
# Project Imports:
from . import models

class AuthorBooksAdminInline(admin.TabularInline):
    model = models.Author.books.through
    

class PublisherBooksAdminInline(admin.TabularInline):
    model = models.Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [AuthorBooksAdminInline, ]
    list_display = [
        'name',
        'birth_date',
        ]
    list_display_links = list_display
    fieldsets = [
        ("Author's Details", {'fields': [
            'name',
            'birth_date',
            ]}
         ),
        ]
    
    
class PublisherAdmin(admin.ModelAdmin):
    inlines = [PublisherBooksAdminInline, ]
    list_display = [
        'name',
        'established',
        ]
    list_display_links = list_display
    fieldsets = [
        ("Publisher's Details", {'fields': [
            'name',
            'established',
            ]}
         ),
        ]
    
    
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'publish_date',
        'book_authors',
        'publisher',
        ]
    list_display_links = list_display
    
    def book_authors(self, obj):
        return [str(author) for author in obj.authors.all()]
    

# Unregister Group and User models from admin
admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)