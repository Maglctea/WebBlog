from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Category
from .forms import NewsForm, UserRegisterForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


def login(request):
    return render(request, 'news/login.html')


def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})

class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'  # ссылка страницы
    context_object_name = 'news'  # передача статичных данных
    # extra_context = {"title": "Главная"}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Передача динам данных """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        """ Уточннение запроса через фильтрацию данных """
        return News.objects.filter(is_bublished=True).select_related('category')



class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'  # ссылка страницы
    context_object_name = 'news'  # передача статичных данных
    allow_empty = False  # вывод пустого списка

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Передача динам данных """
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        """ Уточннение запроса через фильтрацию данных """
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_bublished=True)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'  # передача статичных данных
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'

class CreateNews(LoginRequiredMixin, CreateView):
    '''Класс создания новости'''
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('main') # вариант с переводом на главную страницу после публикации новости

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, 'news/category.html', context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'item': news_item
    }
    return render(request, 'news/view_news.html', context)

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#
#     context = {
#         "form": form
#     }

    return render(request, 'news/add_news.html', context)