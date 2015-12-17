from django.contrib import admin

from .models import Recipient

class RecipientAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'family_relationship',
              'personalized_greeting']
    list_filter = ['last_name']
    list_display = ('first_name', 'last_name', 'family_relationship')

admin.site.register(Recipient, RecipientAdmin)
