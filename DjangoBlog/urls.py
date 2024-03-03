from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
    path('blog/', include('blog.urls', namespace='blog')),  # http://127.0.0.1:8000/blog/
]
