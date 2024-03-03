from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),  # http://127.0.0.1:8000/blog/
    path('<int:id>', views.post_detail, name='post_detail'),  #
]
