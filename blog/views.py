from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

DJANGO_FEATURES = [
    "MTV 패턴: Model(데이터) / Template(화면) / View(로직)로 역할이 나뉨",
    "ORM: SQL을 직접 안 써도 Post.objects.all()처럼 DB를 다룰 수 있음",
    "Admin: 관리자 페이지가 기본 제공되어 글/유저를 바로 관리 가능",
    "Migration: 모델 변경을 DB에 안전하게 반영(makemigrations/migrate)",
]

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {
        "posts": posts,
        "features": DJANGO_FEATURES,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})
