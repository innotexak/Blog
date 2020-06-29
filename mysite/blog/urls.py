from .import views
from django.conf import settings  
from django.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('/', views.feedback, name='feedback'),
    path('/&', TemplateView.as_view(template_name='about.html'), name='about'),
    path('/&/', TemplateView.as_view(template_name='policy.html'), name='policy'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)