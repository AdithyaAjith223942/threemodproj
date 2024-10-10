from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home, name='Home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('smartwatches/', views.smartwatches, name='smartwatches'),
    path('laptop/', views.laptop, name='laptop'),
    path('desktops/', views.desktops, name='desktops'),
    path('graphicscards/', views.graphicscards, name='graphicscards'),
    path('buy/', views.buy, name='buy'),
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:ct>/', views.remove, name='remove'),
    path('increment_quantity/<int:pk>/', views.increment_quantity, name='increment_quantity'),
    path('decrement_quantity/<int:pk>/', views.decrement_quantity, name='decrement_quantity'),
    # path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('view_products/', views.view_products, name='view_products'),
    path('view_users/', views.view_users, name='view_users'),
    path('logout/', views.logout, name='logout'),
    path('category_add/', views.category_add, name='category_add'),
    path('product_add/', views.product_add, name='product_add'),
    path('userpanel/', views.userpanel, name='userpanel'),
    # path('checkout/', views.checkout, name='checkout'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('category_detail/<int:pk>/', views.category_detail, name='category_detail'),
    
]