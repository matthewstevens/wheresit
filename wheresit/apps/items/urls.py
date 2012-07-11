from django.views.generic import DetailView
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from models import Item

import views

urlpatterns = patterns('',
    url(r"^(?P<pk>\d+)$", DetailView.as_view(model=Item, template_name="items/item.html"), name="item_display"),
    url(r"create_item$", views.CreateItemView.as_view(), name="item_new"),
    url(r"add_to_collection/(?P<pk>\d+)$",views.AddToCollectionView.as_view(), name="add_to_collection"),
    url(r"list_items$", views.ListItemView.as_view(), name="item_list"),
    url(r"search_items$", views.SearchFormView.as_view(), name="item_search"),
)
