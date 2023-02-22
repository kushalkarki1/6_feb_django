from django.shortcuts import render, reverse, get_object_or_404
from post.models import Post, Status
from post.forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.filter(status=Status.PUBLIC).order_by("-created_at")
    context = {"posts": posts}
    return render(request, "home.html", context)


@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.add_message(request, messages.INFO, "Your post created successfully.")
        return HttpResponseRedirect(reverse("post:home"))
    context = {"form": form}
    return render(request, "post.html", context)

@login_required
def edit_post(request, postid):
    # try:
    #     post = Post.objects.get(id=postid, user=request.user)
    # except Post.DoesNotExist:
    #     raise Http404()
    post = get_object_or_404(Post, id=postid, user=request.user)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.add_message(request, messages.INFO, "Your post updated successfully.")
        return HttpResponseRedirect(reverse("post:home"))
    return render(request, "post.html", {"form": form})


@login_required
def delete_post(request):
    postid = request.POST.get("postid")
    post = get_object_or_404(Post, id=postid)
    post.delete()
    messages.add_message(request, messages.INFO, "Your post removed successfully.")
    return HttpResponseRedirect(reverse("post:home"))