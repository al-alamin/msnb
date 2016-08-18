from django.contrib import admin
from event.models import Event,Registration

# Register your models here.
class RegistrationInline(admin.TabularInline):
    model = Registration

class EventAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]

admin.site.register(Event,EventAdmin)
admin.site.register(Registration)