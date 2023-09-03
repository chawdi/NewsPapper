from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
# Create your views here.


def news_list(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'news_list.html', {'news': news})


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news_detail.html', {'news': news})


def news_search(request):
    date_filter = request.GET.get('date_filter')
    title_filter = request.GET.get('title_filter')
    author_filter = request.GET.get('author_filter')

    news_queryset = News.objects.all()

    if date_filter:
        news_queryset = news_queryset.filter(pub_date__gte=date_filter)

    if title_filter:
        news_queryset = news_queryset.filter(title__icontains=title_filter)

    if author_filter:
        news_queryset = news_queryset.filter(author__username__icontains=author_filter)

    paginator = Paginator(news_queryset, 10)
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news_search.html', {'news': news})