from django.urls import path
from django.conf.urls import url
from .views import IndexView

urlpatterns = [
        url('$', IndexView.as_view(), name='index_view'),
]
