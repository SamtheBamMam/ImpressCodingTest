from django.contrib import admin

from api.models import ButtonCall


class ButtonCallAdmin(admin.ModelAdmin):
    list_display = ['user', 'fat_count', 'stupid_count', 'dumb_count']


admin.site.register(ButtonCall, ButtonCallAdmin)