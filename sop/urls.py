from django.conf.urls import url
from .views import sop

urlpatterns = [
    url(r'^$', sop, name='sop_review'),
]
