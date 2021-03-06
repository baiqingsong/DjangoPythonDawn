from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^article_page/(?P<article_id>[0-9]+)', views.article_page, name='article_page'),
    url(r'^edit_page/(?P<article_id>[0-9]+)', views.edit_page, name='edit_page'),
    url(r'^edit_action/', views.edit_action, name='edit_action'),
]