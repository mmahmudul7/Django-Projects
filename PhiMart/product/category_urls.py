from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductCategories.as_view(), name='category-list'),
    # path('<int:id>/', views.ViewSpecificCategory.as_view(), name='view-specific-category'),
    path('<int:pk>/', views.CategoryDetails.as_view(), name='view-specific-category'),
]