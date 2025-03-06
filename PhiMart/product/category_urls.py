from django.urls import path
from product import views

urlpatterns = [
    # path('', views.view_categories, name='category-list'),
    path('', views.ViewCategories.as_view(), name='category-list'),
    # path('<int:pk>/', views.view_specific_category, name='view-specific-category'),
    path('<int:id>/', views.ViewSpecificCategory.as_view(), name='view-specific-category'),
]