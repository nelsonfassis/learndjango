from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    context_dict = {
        "key1" : "About View Page",
        "key2" : "Something else",
        "key_list": ["value1", "value2", "value3"]
    }
    return render(request, "about.html", context_dict )    

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")