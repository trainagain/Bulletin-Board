from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import *

urlpatterns = [
   path('', views.HomeList, name='HomeList'),
   # path('edit/', CommentUpdate.as_view(), name='update'),
   # path('delete/', CommentDelete.as_view(), name='delete'),
   # path('news/create/', CommentCreate.as_view(), name='news_create'),
   # path('search/', SeeArchive.as_view()),
   # path('search/<int:pk>/', AdvtDitail.as_view()),
   # path('news/', News.as_view(), name='news_list'),
   # path('news/<int:pk>/', NewsDitail.as_view(), name='news_detail'),
   # path('news/create/', NewsCreate.as_view(), name='news_create'),
   # path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
   # path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   # path('advt/', Advt.as_view(), name='advt_list'),
   # path('advt/<int:pk>/', AdvtDitail.as_view(), name='advt_detail'),
   # path('advt/create/', AdvtArCreate.as_view(), name='advt_create'),
   # path('advt/<int:pk>/edit/', AdvtUpdate.as_view(), name='advt_update'),
   # path('advt/<int:pk>/delete/', AdvtDelete.as_view(), name='advt_delete'),
   # path('subscriptions/', subscriptions, name='subscriptions'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)