from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('search', views.search, name="search"),
    path("<int:id>/<slug:slug>", views.productDetail, name="productDetail"),
    path('addcomment/<int:id>', views.addComment, name="addComment"),
]
