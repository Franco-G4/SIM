
# from django.shortcuts import render
# from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView 
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse
# from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin

# from django import forms
# from django.http import HttpResponse

class home(TemplateView):
    template_name = 'HomePage/body.html'
# Create your views here.

