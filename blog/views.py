from django.shortcuts import render
from blog.models import Category, Blog

# Create your views here.

def index(request):
    context = {
        "categories": Category.objects.all(),
    }
    # print(request.META["HTTP_X_REAL_IP"])
    # print(request.META["REMOTE_ADDR"])
    return render(request, "blog/index.html", context)

def blog_details(request, slug):
    
    blog = Blog.objects.get(slug=slug)

    context = {
        "blog": blog,
        "categories": Category.objects.all(),
        "images": [blog.image_one, blog.image_two, blog.image_three, blog.image_four, blog.image_five,],
    }
        
    return render(request, "blog/blog_details.html", context)

def blog_by_category(request, slug):
    
    context = {
        #  "blogs": Blog.objects.filter(is_active=Tre, category__slug=slug),
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug,
    }
    return render(request, "blog/blog.html", context)