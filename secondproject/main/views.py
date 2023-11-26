from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

from main.models import Article
from .forms import *

def is_superuser(user):
    return user.is_superuser

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'main/article_confirm_delete.html'
    success_url = reverse_lazy('home')

    @method_decorator(user_passes_test(is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class IndexHome(ListView):
    paginate_by = 5
    model = Article
    template_name = 'main/index.html'
    context_object_name = 'data'
    ordering = ['-time_create']
    
    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by('-time_create')

def signin(request):
    return render(request, 'main/signin.html')

def login(request):
    return render(request, 'main/login.html')

class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'main/createpost.html'
    

class PostDetailView(DetailView):
    model = Article
    template_name = 'main/post_detail.html'

    def get_object(self, queryset=None):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Article, id=post_id)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/signin.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('home')
    
    
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"
    
    def get_success_url(self):
        return reverse_lazy('home')
    
def logout_user(request):
    logout(request)
    return redirect('home')

def error_404(request, exception):
    return render(request, '404.html', status=404)