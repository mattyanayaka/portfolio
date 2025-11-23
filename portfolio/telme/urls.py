from django.conf.urls import url
from .views import TelmeView

urlpatterns = [
    url(r'', TelmeView.as_view(), name='index'),
]