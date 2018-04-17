from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<a href='/help'><h1 align='center'>My Second App</h1></a>")



def help(request):
    insert_me = {'insert_me':"I am imported here!:D"}
    return render(request, "AppTwo/index.html",context=insert_me)