from django.urls import path

from .views import (
                        # create_article_view,
                        ArticleCreateView,
                        ArticleUpdateView,
                        ArticleDeleteView,
                        # article_list_view,
                        ArticleListView,
                        ArticleDetailView,
                        # article_detail_view,
                    )

app_name = 'Blog'
urlpatterns = [
    # path('create/',create_article_view),
    path('create/',ArticleCreateView.as_view()),
    path('<int:id>/update/',ArticleUpdateView.as_view(), name='article_update_view'),
    # path('',article_list_view, name='article_list_view'),
    path('', ArticleListView.as_view(), name='article_list_view'),
    # path('<int:id>/',article_detail_view, name='article_detail_view'),
    path('<int:id>/',ArticleDetailView.as_view() , name='article_detail_view'),
    path('<int:id>/delete/',ArticleDeleteView.as_view() , name='article_delete_view'),
]