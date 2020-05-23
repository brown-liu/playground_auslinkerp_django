from django.conf.urls import url

from Daily_KPI import views

urlpatterns = [
    url(r"^dkhp", views.dkhp, name='dkhp')
]
