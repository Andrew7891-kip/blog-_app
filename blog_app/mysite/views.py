from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator
# Create your views here.
def post(request):
    posts=Post.objects.filter(status=1)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 
    # return render(request, 'list.html', {'page_obj': page_obj})

    return render(request,'post.html', {'page_obj': page_obj})

# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage 
# def PostList(request): 
#     object_list = Post.objects.filter(status=1).order_by('-created_on') 
#     paginator = Paginator(object_list, 3) # 3 posts in each page page = request.GET.get('page') 
#     try: post_list = paginator.page(page) 
#     except PageNotAnInteger: 
#         # If page is not an integer deliver the first page 
#         post_list = paginator.page(1) 
#     except EmptyPage: # If page is out of range deliver last page of results 
#     post_list = paginator.page(paginator.num_pages) 
#     return render(request, 'index.html', {'page': page, 'post_list': post_list})

def post_detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'details.html',{'post':post})

def post_form(request,pk):
    post=Post.objects.get(pk=pk)
    comments=post.comments.filter(active=True)
    new_comment=None
    if request.method == 'POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_form=CommentForm()
    context={
        'post':post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form
    }
    return render(request,'details.html',context)
