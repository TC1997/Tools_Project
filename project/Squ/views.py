from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the Squ  index.")
def update(request,id):
    response="aaa%s"
    return HttpResponse(response %id)
def map(request):
    return HttpResponse("Hello, world. You're at the Squ  map.")
def add(request):
    return HttpResponse("Hello, world. You're at the Squ  update.")
def sightings(request):
    return HttpResponse("Hello, world. You're at the Squ  sightings.")
def stats(request):
    return HttpResponse("Hello, world. You're at the Stats  stats.")
# Create your views here.
