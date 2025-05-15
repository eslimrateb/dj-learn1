from django.shortcuts import render, redirect
from .models import Post
from .forms import Post_forms

# Create your views here.


def post_list(request):
    data = Post.objects.all()
    return render(request, 'post_list.html', {'post': data})


def post_details(request, post_id):
    data = Post.objects.get(id=post_id)
    return render(request, 'post_details.html', {'post': data})


def post_new(request):
    if request.method == 'POST':
        form = Post_forms(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/blog')

    else:
        form = Post_forms()

    return render(request, 'post_new.html', {'post': form})


def post_edit(request, post_id):
    data = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = Post_forms(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/blog')

    else:
        form = Post_forms(instance=data)

    return render(request, 'post_edit.html', {'post': form})


def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('/blog')
