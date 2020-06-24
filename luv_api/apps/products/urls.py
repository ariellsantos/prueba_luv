from django.urls import path

from .views import ProductsBulkPostView

app_name = 'products'

urlpatterns = [
    path('products/bulk_insert', ProductsBulkPostView.as_view()),
]
