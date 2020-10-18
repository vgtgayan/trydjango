from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article
# Create your views here.
# def article_detail_view(request, id):
#     obj = Article.objects.get(id=id)
#     context = {
#         'object': obj
#     }
#     return render(request, 'article_detail.html', context)
class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=obj_id)

# def article_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, 'article_list.html', context)
class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()
    

class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '../create/'

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'

class ArticleUpdateView(UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '../create/'

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=obj_id)

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    # queryset = Article.objects.all()
    # success_url = '../../'
    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=obj_id)

    def get_success_url(self):
        return reverse('Blog:article_list_view')

# def create_article_view(request):
#     form = ArticleModelForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ArticleModelForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'article_create.html', context)