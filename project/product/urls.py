from django.urls import path

from .views import CategoryCreateView,ProductView

urlpatterns = [
    path('',CategoryCreateView.as_view(),name='category'),
    path('<pk>/',CategoryCreateView.as_view(),name='category'),
    path('product/<pk>/',ProductView.as_view(),name='product')
]