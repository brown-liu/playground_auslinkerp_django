from django.conf.urls import url

from app import views

urlpatterns = [
    url(r"^success/", views.successPage, name="success"),
    url(r'^change_onhold/', views.change_onhold_status, name='change_onhold_status'),

    # url(r'^mine/',views.mine,name='mine'),
    # url(r'^logout',views.logout,name='logout')

]
