from django.conf.urls import url

from clientdatabases import views

urlpatterns = [

    url(r"^clientdatabases", views.clientdatabases, name='clientdatabases'),
    url(r'^change_status_post/', views.change_onhold_status, name='change_onhold'),
    url(r'^importafile/', views.importafile, name='importafile'),
    url(r"^quicklink/", views.quicklink, name='quicklink'),
    url(r'^upload/', views.uploadfile, name='uploadfile'),
    url(r"^clientdbhp/", views.clientdbhp, name='clientdbhp'),
    url(r'^customerstockreport/', views.uploadfile_customer_stock, name='uploadfile_customer_stock')
]
