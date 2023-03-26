from django.contrib import admin
from .models import Proyect
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proyect,ProjectAdmin)
