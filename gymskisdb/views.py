from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import gym

# Create your views here.

def index(request):
    top_ten_list = gym.objects.order_by("rating")[:10]
    output = ", ".join([g.name for g in top_ten_list])
    context = {"name" : output}
    template = loader.get_template("gymskisdb/index.html")
    return HttpResponse(template.render(context, request))

def post(request):
    top_ten_list = gym.objects.order_by("rating")[:10]
    output = ", ".join([g.name for g in top_ten_list])
    context = {"name" : output}
    template = loader.get_template("gymskisdb/index.html")
    return HttpResponse(template.render(context, request))
