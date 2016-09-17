from django.conf.urls import url, include
from .views import about_us

urlpatterns = [
    url(r'^$', about_us, name='about_us')
]
