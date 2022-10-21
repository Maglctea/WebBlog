from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('test/', test, name='test'),
    # path('', index, name='main'),
    path('', HomeNews.as_view(), name='main'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('category/<int:category_id>', NewsByCategory.as_view(),
         name='category'),
    # path('news/<int:news_id>', view_news, name='view_news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    # path('news/add-news>', add_news, name='add_news'),
    path('news/add-news>', CreateNews.as_view(), name='add_news'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

