from django.shortcuts import render
from things.forms import PostForm

def home(request):
    form = PostForm(request.POST or None)
    return render(request, 'home.html', {'form': form})
