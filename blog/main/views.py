from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 


def post_list(request):
    all_post = Post.published.all()
    
    paginator = Paginator(all_post, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)


    data = {
        # 'page': page,
        "posts":posts
    }
    
    return render(request, "post/list.html", data)



def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,  slug=slug,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    
    return render(request, "post/detail.html", {"post":post})
    

