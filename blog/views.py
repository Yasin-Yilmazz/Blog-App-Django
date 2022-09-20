from multiprocessing import context
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    qs = Post.objects.all()
    context = {
        "object_list":qs
    }
    return render(request, "blog/post_list.html", context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:list")
    context = {
        "form":form
    }
    return render(request, "blog/post_create.html", context)