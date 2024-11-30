'''from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link
# Create your views here.
# instead of function, we create a class 
class LinkListView(ListView):
    model = Link #This line does the role of the lines bellow :

    # links = Link.objects.all()
    # context = {'links': links}
    # return render(request,'link_list.html',context)

class LinkCreateView(CreateView):
    # create forms.py file & form
    # check if this was a post or get request
    # return an empty form or save the fprm data
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # template model_form -> link_form.html

class LinkUpdateView(UpdateView):
    # create a form
    # check if a get request or a put request
    # either render the form or update and save it in our db
    model = Link
    fields = ['text','url']
    success_url = reverse_lazy('link-list')

class LinkDeleteView(DeleteView):
    # take in a id/pk of an object
    # query to db for that object
    # check if it exists -> delete the object
    # return some template or forward to user to some url
    model = Link
    success_url = reverse_lazy('link-list')
    # form to submit to delete the item
    # except a template named link_confirm_delete.html

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)'''
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link

# INTERNAL
# list out the links 
# create a new link

# EXTERNAL
# see a profile (and it's links)

class LinkListView(ListView):
    model = Link
    #def template model_list.html

class LinkCreateView(CreateView):
    model = Link
    # template - model_form.html
    # figure out what fields - could pass a list
    fields = "__all__"
    #success_url
    success_url = reverse_lazy('link-list')

class LinkUpdateView(UpdateView):
    # Shares same template as create view
    model = Link
    fields = ["text", "url"]
    success_url = reverse_lazy('link-list')

class LinkDeleteView(DeleteView):
    #send a form with a single 'confirm delete btn'
    # template - model_confirm_delete.html
    model = Link
    success_url = reverse_lazy('link-list')

## external profile view - could be a ListView or a function view
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)