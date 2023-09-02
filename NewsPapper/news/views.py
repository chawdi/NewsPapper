from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404
# Create your views here.


def news_list(request):
    news = News.objects.order_by('-pub_date')
    return render(request, 'news_list.html', {'news': news})


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news_detail.html', {'news': news})