from django.urls import path
from . import views

urlpatterns = [
    # path('add_people/', views.add_people),
    path('EditProfileView/<int:id>/',
         views.EditProfileView, name="EditProfileView"),
    path('product_list', views.product_list.as_view(), name="product_list"),
    path('PasswordChangeView/<int:pk>/',
         views.PasswordChangeView.as_view(), name='PasswordChangeView'),
    path('about_us', views.about_us.as_view(), name='about_us'),
    path('contact', views.contact.as_view(), name='contact'),
    path('single_product/<int:pk>/',
         views.single_product.as_view(), name='single_product'),
    path('shop_list/<int:id>/', views.shop_list, name='shop_list'),
    path('product_cart/', views.product_cart, name='product_cart'),
    path('wishlistView/', views.wishlistView.as_view(), name='wishlistView'),
    path('addcart/', views.addcart, name='addcart'),
    path('load_header/', views.load_header, name='load_header'),

]
