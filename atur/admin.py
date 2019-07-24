from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_file', 'tanggal', 'tanggalinput', 'jam','jaminput','integ','isi','tempat']

admin.site.register(Blog, BlogAdmin)