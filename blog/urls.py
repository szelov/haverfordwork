from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^scottie/$', views.scottie_page, name='scottie_page')
#    url(r'^alex/$', views.alex_page, name='alex_page')
#    url(r'^payton/$', views.payton_page, name='payton_page')
]