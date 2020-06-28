"""auslinkerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib import staticfiles
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r"^homepage/", views.homepage, name='homepage'),
    url(r"^setcompanystatus/", views.setCompanyStatus, name='setcompanystatus'),
    url(r'^app/', include('app.urls')),
    url(r'^staff_user/', include(('staff_user.urls', 'staff_user'), namespace='staff_user')),
    url(r'^search-post$', views.search_post, name='searchposted'),

    url(r'^clientdataentry/', views.clientDataEntry, name='client_data_entry'),
    url(r'^forwarding/', include('forwarding.urls')),
    url(r'^warehouse/', include(('warehouse.urls', 'warehouse'), namespace='warehouse')),
    url(r'^adminandaccount/', include('adminandaccount.urls')),
    url(r'^Daily_KPI/', include('Daily_KPI.urls')),
    url(r'^clientdatabases/', include('clientdatabases.urls')),
    url(r'^information/',include(('information.urls','information'),namespace='information')),

]
