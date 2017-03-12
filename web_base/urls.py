from __future__ import unicode_literals
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^yahui/', include('yh_base.urls')),
    url(r'^yuntu/', include('yuntu.urls')),
]
