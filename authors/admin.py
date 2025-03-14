from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'bio', 'birth_date', 'nationality']
    search_fields = ['first_name', 'last_name', 'bio', 'nationality']