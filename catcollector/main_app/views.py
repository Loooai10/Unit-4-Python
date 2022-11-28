from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views.generic.edit import CreateView
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the FeedingForm
from .forms import FeedingForm
from .models import Cat
# ...
class CatUpdate(UpdateView):
      model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
      fields = ['breed', 'description', 'age']
      success_url = '/cats/'

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

class CatCreate(CreateView):
      model = Cat
      fields = '__all__'
      success_url='/cats/'
# class CatCreate(CreateView):
#       model = Cat
#       fields = ['name', 'breed', 'description', 'age']
        

# update this view function
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    # include the cat and feeding_form in the context
    'cat': cat, 'feeding_form': feeding_form
  })


def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })

def add_feeding(request, cat_id):
      # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

# class Cat:
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

# View functions

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def cats_index(request):
#   return render(request, 'cats/index.html', { 'cats': cats})