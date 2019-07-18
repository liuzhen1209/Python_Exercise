
from django.conf.urls import include, url
from django.contrib import admin
from hero import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', views.index),
    url(r'^hero/(\d+)', views.glorydetail),
    url(r'^delete/(\d+)', views.glorydelete),
    url(r'^add', views.gloryadd),
]
