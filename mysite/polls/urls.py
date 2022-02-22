from django.urls import path
from . import views

urlpatterns = [
    path('',views.page_top,name='page_top'),
    path('menu01/',views.page_menu,name='page_menu01')
]