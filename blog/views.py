from django.shortcuts import render
from blog.models import BlogPost, Comment
from blog.forms import CommentForm
# Create your views here.

def blog_index(request):
    blog_posts = Post.objects.all().order_by('-created_on')
    context = {
        "blog_posts": blog_posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    blog_posts = BlogPost.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "blog_posts": blog_posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                blog_post=blog_post
            )
            comment.save()

    comments = Comment.objects.filter(blog_post=blog_post)
    context = {
        "blog_post": blog_post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)
