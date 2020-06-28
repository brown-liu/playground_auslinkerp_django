from django.conf.urls import url

from information import views

urlpatterns=[
    url(r'^training_f/',views.training_forwarding,name='training_forwarding'),
    url(r'^training_l/',views.training_logistics,name='training_logistics'),

]