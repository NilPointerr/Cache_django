from django.contrib import admin
from django.urls import path,include
from .views import temp_1,view_cache
from caching1 import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('',cache_page(30)(temp_1.as_view()),name = 'home'),
    path('view',views.view_cache,name="view")


]
