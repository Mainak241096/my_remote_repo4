from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from cbvapp.models import Beer
# Create your views here.
class DrinkListView(ListView):
    model = Beer
    #default template_name = beer_list.html
    #default context_object_name = beer_list
class DrinksCreateView(CreateView):
    model = Beer
    fields = '__all__'
    #default template_name = beer_form.html
class DrinksDetailView(DetailView):
    model = Beer
    #default template_name = beer_detail.html
    #default context_object_name = beer or object
class DrinksUpdateView(UpdateView):
    model = Beer
    fields = '__all__'
    # default template_name = beer_form.html
    # default context_object_name = beer or object

from django.urls import reverse_lazy
class DrinksDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('list')
    # default template_name = beer_confirm_delete.html
    # default context_object_name = beer or object


# Note: Before run, we have to makemigrations and migrate the project
