from django.shortcuts import render
def home(request):
    return  render(request,"index.html")
def form(request):
    return  render(request,"form.html")
def blog(request):
    return  render(request,"blog.html")
# Create your views here.
