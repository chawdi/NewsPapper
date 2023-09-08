from .models import News
from .forms import NewsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.


def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news:news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news_create.html', {'form': form})


def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save()
            return redirect('news:news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_edit.html', {'form': form, 'news': news})


def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news:news_list')
    return render(request, 'news_delete.html', {'news': news})


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


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
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
