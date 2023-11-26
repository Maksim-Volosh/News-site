from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls import handler404

urlpatterns = [
    path('', IndexHome.as_view(), name='home'),
    path('accounts/signin/', RegisterUser.as_view(), name='signin'),
    path('accounts/login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('createpost/', AddPost.as_view(), name='createpost'),
    path('delete_post/<int:pk>/', ArticleDeleteView.as_view(), name='delete_post'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
]

handler404 = "main.views.error_404"
