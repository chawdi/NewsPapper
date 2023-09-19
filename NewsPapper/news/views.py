from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import News
from .forms import NewsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news_create.html'
    success_url = reverse_lazy('news:news_list')


class NewsEditView(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news:news_list')


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news:news_list')


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 10


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'


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

