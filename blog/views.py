from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    # DB에서 모든 글을 가져와서(objects.all)
    posts = Post.objects.all().order_by('-created_at')
    # post_list.html 템플릿에 전달한다
    return render(request, 'blog/post_list.html', {'posts': posts})