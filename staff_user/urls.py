from django.conf.urls import url

from staff_user import views

urlpatterns = [

    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^removestaff/', views.removestaff, name='removestaff'),
    url(r'^worktime/', views.worktime, name='worktime'),
    url(r'^work/', views.work, name='startwork'),

]
