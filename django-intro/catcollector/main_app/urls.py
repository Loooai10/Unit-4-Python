from django.urls import path
from . import views
# . represent all the items
urlpatterns = [
  path('home', views.home, name='home'),
  path('about/', views.about),
  path('contact', views.contact),
]
# yous can put '' as in empty it leads to home also