from django.conf.urls import url

from warehouse import views

urlpatterns = [

    url(r'^whhp/', views.whhp, name='whhp'),
    url(r'^container_upload_info/', views.container_upload_info, name='container_upload_info'),
    url(r'^containerregisterpage/', views.containerregister, name='containerregisterpage'),
    url(r'^warehouseinfo/', views.warehouseinfo, name='warehouseinfo'),

    url(r'^weeklychecksheet', views.weeklychecksheet, name='weeklychecksheet'),
]
