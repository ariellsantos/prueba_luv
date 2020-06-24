from django.urls import path

from .views import ProductsBulkPostView, ProductsListGetView

app_name = 'products'

urlpatterns = [
    path('products/bulk_insert', ProductsBulkPostView.as_view()),
    path('products', ProductsListGetView.as_view()),
]
