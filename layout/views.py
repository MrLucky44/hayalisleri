from django.shortcuts import render 
from blog.models import Category

# Create your views heregggg.

def index(request):
    context = {
        "categories": Category.objects.all()
    }
    return render(request, "layout/index.html", context)