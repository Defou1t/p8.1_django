from django.conf.urls import url
import mygis.views

urlpatterns = [
    url(r'^$', mygis.views.home, name='home'),
    url(r'^map/$', mygis.views.map_my, name='map'),
    url(r'^about/$', mygis.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', mygis.views.show_articles, name='article'),
]