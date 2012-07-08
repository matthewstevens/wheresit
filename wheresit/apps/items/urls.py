from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

import views

urlpatterns = patterns('',
    url(r"create_item$", views.CreateItemView.as_view(), name="item_new"),
    url(r"list_items$", views.ListItemView.as_view(), name="item_list"),
)
