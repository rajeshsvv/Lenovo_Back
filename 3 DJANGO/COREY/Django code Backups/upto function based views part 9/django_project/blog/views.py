from django.shortcuts import render
from .models import Post  # existss in the same directory thats why use .(blog)
# from django.http import HttpResponse for return the HttpResponse


def home(request):
    context = {
        # "posts": posts
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def about(request):
    # return HttpResponse("<h1>Blog About</h1>")
    return render(request, "blog/about.html", {"title": "About"})

# html structure to find django to map templates            blog->templates->blog->template.
