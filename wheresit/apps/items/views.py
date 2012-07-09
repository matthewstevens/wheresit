from django.views.generic import CreateView, DetailView, FormView, ListView, TemplateView
from forms import ItemForm, ItemSearchForm
from models import Item

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
