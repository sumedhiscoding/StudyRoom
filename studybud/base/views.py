from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # so the request object is going to be http object which tells us what kind of request method is going to be sent
    # what kind of data is passed in what kind of data user is sending
    return render(request,'home.html')

def room(request):
    return render(request,"room.html")
