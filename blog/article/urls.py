
from django.urls import path
from article.views import index, about, detail

# 127:0.0.1:8000/articles/
urlpatterns = [
    # 127:0.0.1:8000/articles/article/5
    path('article/<int:id>', detail, name='detail')  # Dinamik URL
]
