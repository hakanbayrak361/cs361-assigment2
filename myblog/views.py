from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import my_blog

def show_blog(request):

    if request.method == "POST":
        my_blog.objects.create(name=request.POST.get("header_input"),
                            description=request.POST.get("body_input"))

    return render(request, "my_entry.html", {"todos": my_blog.objects.all()})


def get_blog(request, todo_id):
    try:
        todo = my_blog.objects.get(id=todo_id)
        return render(request, "exstra.html", {"todo": my_blog})
    except my_blog.DoesNotExist:
        raise Http404("We don't have any.")
