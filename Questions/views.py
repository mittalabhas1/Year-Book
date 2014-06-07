from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView, ListView

class IndexView(generic.ListView):

class QuestionView(generic.DetailView):

def saveAnswer(request):