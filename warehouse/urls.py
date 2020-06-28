from django.conf.urls import url

from warehouse import views

urlpatterns = [

    url(r'^whhp/', views.whhp, name='whhp'),
    url(r'^container_upload_info/', views.container_upload_info, name='container_upload_info'),
    url(r'^containerregisterpage/', views.containerregister, name='containerregisterpage'),
    url(r'^warehouseinfo/', views.warehouseinfo, name='warehouseinfo'),

    url(r'^weeklychecksheet/', views.weeklychecksheet, name='weeklychecksheet'),

    url(r'^updatetimestamp/', views.update_timestap, name='update_time_stamp'),
    url(r'^update_chart/', views.update_chart, name='update_chart'),
    url(r"^change_container_status/", views.change_container_status, name='change_container_status'),
    url(r'^container_detail_ajax/', views.container_detail_ajax, name="container_detail_ajax"),
    url(r'^markjobdone/', views.mark_job_done, name="mark_job_done"),
    url(r'^delete_container/',views.delete_container,name='delete_container')
]
