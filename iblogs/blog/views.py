from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.

def home(request):
    #load all the post from db(eg.10 )
    posts = Post.objects.all()[:11]
    # print(posts )
    data = {
        'posts': posts
    }
    return render(request, 'home.html', data)


def post(request,url):
    post = Post.objects.get(url=url)
    return render(request, 'posts.html', {'post': post})