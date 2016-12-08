from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import my_entry

def show_blog(request):
    return render(request, "my_blog.html", {"entries": my_entry})


def get_blog(request, todo_id):
    try:
        return HttpResponse(my_entry[int(todo_id)])
    except IndexError:
        raise Http404("We don't have any.")