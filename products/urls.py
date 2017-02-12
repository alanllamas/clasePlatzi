from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^$', view=views.hello_world, name='hello world'),
    url(regex=r'^product/(?P<pk>[0-9]+)/$', view=views.product_detail, name='product_detail'),
    url(regex=r'^product/new/$', view=views.new_product, name='new_product'),
]
