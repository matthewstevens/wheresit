from django.views.generic import CreateView, \
        DetailView, \
        FormView, \
        ListView, \
        RedirectView, \
        TemplateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django import http
from forms import ItemForm, ItemSearchForm
from models import Item, OwnedItem
from apps.profiles.models import Profile

class CreateItemView(CreateView):
    template_name = "items/item_new.html"
    form_class = ItemForm
    success_url = 'create_item'

class ListItemView(ListView):
    template_name = "items/item_list.html"
    model = Item

class SearchFormView(FormView):
    template_name = "items/item_search.html"
    form_class = ItemSearchForm
    success_url = "search_items"
    def form_valid(self, form):
        """ Consider using haystack, woosh or equivalent """
        context = self.get_context_data(form=form)
        name_search = form.cleaned_data['name_search']
        tags_search = form.cleaned_data['tags_search']
        results = Item.objects.all()
        if name_search:
            results = results.filter(name=name_search)
        if tags_search:
            results = results.filter(meta_tags=tags_search)
        context['items'] = results
        return self.render_to_response(context)

class AddToCollectionView(RedirectView):
    url = "../%(pk)"
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if request.user:
            profile = Profile.objects.get(user=request.user)
            item = get_object_or_404(Item, pk=pk)
            owned_item = OwnedItem.objects.get_or_create(item = item, user = profile)
            # at this point we probably want to redirect to the owned item page
        return http.HttpResponseRedirect(reverse("item_display", kwargs={'pk': item.pk}))
        #return self.get(request, *args, **kwargs)
