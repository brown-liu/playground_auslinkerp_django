from django.conf.urls import url

from forwarding import views

urlpatterns = [
    url(r'^fwdhp', views.fwdhp, name='fwdhp')
]
