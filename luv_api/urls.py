from django.urls import path, include

urlpatterns = [
    path('api/', include('luv_api.apps.products.urls', namespace='products')),
]
