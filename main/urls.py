from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', BaseView, name='baseview'),
    path('register-customer/', RegisterCustomerView, name = 'customer-create'),
    path('update-customer/', UpdateCustomerView, name = 'customer-update'),
    path('products/all/', listAll, name = 'products-view'),
    path('products/<str:category>/', listCategory, name = 'products-view-category'),
    path('cart/', CartView, name = 'cart-view'),



    # path('products/<str:category>/<int:id>', ProductDetailView, name = 'product-detail'),
    # path('<int:id>/', PhoneDetailView.as_view(), name = 'phone-detail'),
    # path('upload/', image_request, name = "image-request") ,
    # path('create-seller-profile/', SellerCreateView.as_view(), name = "seller-create") ,
    # path('<int:id>/update-seller-profile/', SellerUpdateView.as_view(), name = "seller-update") ,
    # path('create_product/', ProductCreateView.as_view(), name = "product-create") ,
]

