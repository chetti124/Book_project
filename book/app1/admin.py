from django.contrib import admin

# Register your models here.

from app1.models import Book

admin.site.register([Book])
