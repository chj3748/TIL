from django.shortcuts import render, redirect
from .models import Review
# Create your views here.

def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, 'community/review_list.html',context)

def new_review(request):

    return render(request, 'community/new_review.html')

def create_review(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    rank = request.GET.get('rank')

    review = Review()
    review.title = title
    review.content = content
    review.rank = rank
    review.save()
    print(title,content,rank)
    # return redirect('/community')
    return redirect(f'/community/review_detail/{review.pk}')


def review_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'title' : review.title,
        'content' : review.content,
        'rank' : review.rank,
        'created_at' : review.created_at,
        'updated_at' : review.updated_at,
    }
    return render(request, 'community/review_detail.html', context)

