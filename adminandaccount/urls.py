from django.conf.urls import url

from adminandaccount import views

urlpatterns = [
    url(r'^adminhp/', views.adminhp, name='adminhp')
]
