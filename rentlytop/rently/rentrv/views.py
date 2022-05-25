from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class RvListView(ListView): 
	model = models.Rv 

class RvDetailView(DetailView):
	model = models.Rv 

class RvUpdateView(UpdateView): 
	model = models.Rv 
	fields = "__all__"
	success_url = "/"

class RvCreateView(CreateView): 
	model = models.Rv 
	fields = "__all__"
	success_url = "/"

class RvDeleteView(DeleteView): 
	model = models.Rv
	success_url = "/"




	
