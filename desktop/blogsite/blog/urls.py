from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .import views 
from .views import PostList, SearchResultsView

urlpatterns = [
    path('', views.home, name= "home"),
    path('postdetail/<slug:slug>/', views.post_detail, name="postdetail"),
    # path('reply/<int:id>', views.reply, name="reply"),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('blog/', PostList.as_view(), name="blog"),
    # path('reply/', views.reply, name="reply"),
    path('contact/', views.contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)