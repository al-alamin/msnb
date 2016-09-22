from datetime import timedelta

from django.contrib import admin
from event.models import Event, Registration
from kombu.transport.django import models as kombu_models
from django.utils import timezone

from common.tasks import send_skype_email_after_mintue, send_skype_email_before_hour, send_skype_email_before_mintue
from common.tasks import add

# send_skype_email_before_hour
#     send_skype_email_before_mintue
# Register your models here.


class RegistrationInline(admin.TabularInline):
    model = Registration


class EventAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]
    raw_id_fields = ('presenter', )

    def save_model(self, request, obj, form, change):
        print("\n\n In Event Save Method ")
        obj.save()

        # 12 Hours before the event
        time_hour = obj.start_time - timedelta(hours=12)
        # 30 minutes before the event
        time_minute_before = obj.start_time - timedelta(minutes=30)
        # 30 minutes after the event
        time_minute_after = obj.end_time - timedelta(minutes=30)

        send_skype_email_before_hour.apply_async(
            (obj.id,), eta=time_hour)  # event_id
        send_skype_email_before_mintue.apply_async(
            (obj.id,), eta=time_minute_before)  # event_id, minute
        send_skype_email_after_mintue.apply_async(
            (obj.id,), eta=time_minute_after)

        # send_skype_email_before_mintue.apply_async(
        #     (obj.id,), eta=timezone.now() + timedelta(minutes=2)) 
        
        add.apply_async((15, 5), countdown=5)

admin.site.register(Event, EventAdmin)
admin.site.register(Registration)
admin.site.register(kombu_models.Message)
