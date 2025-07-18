"""
URL configuration for Project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Project1 import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("account/", views.account, name="account"),
    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop, name="shop"),
    path("cart/", views.cart, name="cart"),
    path("single-product/", views.single_product, name="single_product"),
    path("single-blog/", views.single_blog, name="single_blog"),
]
