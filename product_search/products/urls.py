from django.urls import path
from .views import ProductSearchView
from ..product_search.settings import schema_view
app_name = 'products'

urlpatterns = [
    path('search/', ProductSearchView.as_view(), name='product_search'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
