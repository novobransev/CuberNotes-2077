from django.contrib import admin
from .models import Notes


class AdminCreate(admin.ModelAdmin):
    readonly_fields = ('time_create', )

admin.site.register(Notes, AdminCreate)
