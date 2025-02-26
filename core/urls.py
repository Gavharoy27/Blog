from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('blog/', blog_view, name='blog'),
    path('blog_add/', blog_add_view, name='blog_add'),
    path('m_matn/', m_matn_view, name='m_matn'),
]

urlpatterns += [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]