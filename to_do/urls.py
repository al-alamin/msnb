from django.conf.urls import url
from .views import to_do

urlpatterns = [
   url(r'^$',to_do, name='to_do'),
]
