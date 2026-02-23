from django.urls import path
from .views import *

app_name = "blogs"

urlpatterns = [
    path('', list_articles, name='articles_list'),
    # path('', ClassBasedView.as_view(), name='articles_list'),
    path('<int:article_id>/', details_article, name="article_details")
]