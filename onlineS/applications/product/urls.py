from django.urls import path

from applications.product.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home-page'),

]