from django.urls import path
from post.views import *
app_name = 'post'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('detail/<slug>', BlogDetailView.as_view(), name='detail'),
]
