from django.contrib import admin

from chatbot_tutorial.models import ButtonCall


class ButtonCallAdmin(admin.ModelAdmin):
    list_display = ['user', 'fat_count', 'stupid_count', 'dumb_count']


admin.site.register(ButtonCall, ButtonCallAdmin)