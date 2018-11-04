from django.contrib import admin

from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['personid',	'firstname', 'middlename',
                    'lastname',	'email', 'persontype']
