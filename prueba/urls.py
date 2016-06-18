"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from importaciones import views
from django.core.urlresolvers import  reverse_lazy
from importaciones.views import ListRegistroView
from importaciones.views import CreateRegistroView
from importaciones.views import DetailRegistro
from importaciones.views import DeleteRegistro

# Este es el urls en el que debo trabajar.

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$',views.inicio),

    url(r'^login/', 'django.contrib.auth.views.login',
        {'template_name':'login.html'},name='login'),

    url(r'^cerrar/', 'django.contrib.auth.views.logout_then_login',name='logout'),

    url(r'^data/', views.gestion),

    url(r'^archivocsv/$', views.archivocsv, name = "archivocsv"),
    url(r'^registro/$', ListRegistroView.as_view(), name = "registro-list",),
    url(r'^newregistro/$', CreateRegistroView.as_view(), name = "registro-new",),
    url(r'^registro/(?P<pk>\d+)/$', DetailRegistro.as_view(), name = 'registro-view',),
    url(r'^delete/(?P<pk>\d+)/$', DeleteRegistro.as_view(), name = 'registro-delete',),

]
