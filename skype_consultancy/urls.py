from django.conf.urls import url
from .views import skype, delete_skype_registration

urlpatterns = [
    url(r'^$', skype, name='skype'),
    url(r'^withdraw$', delete_skype_registration, name='reg_withdraw'),
]
