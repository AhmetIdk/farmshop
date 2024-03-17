from django.urls import path

from user.views import *



urlpatterns = [
    path("", user_update, name="user_profile"),
    path("update", user_update, name="user_update"),
    path("login", user_login , name="user_login"),
    path("logout", user_logout, name="user_logout"),
    path("register", user_register, name="user_register"),
    path('password/', user_password, name='user_password'),
    path('mycomments/', user_comments, name='user_comments'),
    path('deletecomment/<int:id>', user_delete_comment, name='user_delete_comment'),
    path("favorites", favorites, name="user_favorites"),
    # path('myorders/', user_orders, name='user_orders'),
    path('myorders_products/', user_order_products, name='user_order_products'),
    # path('orderdetail/<int:id>', user_order_detail, name='user_order_detail'),
    # path('order_product_detail/<int:id>/<int:oid>', user_order_product_detail, name='user_order_product_detail'),
]