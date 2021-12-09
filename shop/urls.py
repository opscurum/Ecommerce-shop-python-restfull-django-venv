"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from category import views as category_view
from product import views as product_view
from favourite import views as favourite_view
from slider import views as slider_view

router = routers.DefaultRouter()
router.register(r'category', category_view.CategoryViewSet)
router.register(r'product', product_view.ProductViewSet)
router.register(r'favourite', favourite_view.FavouriteViewSet)
router.register(r'slider', slider_view.SliderViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('product/', include(('product.urls', 'product'), namespace='product')),
    path('category/', include(('category.urls', 'category'), namespace='category')),
    path('slider/', include(('slider.urls', 'slider'), namespace='slider')),
    path('favourite/', include(('favourite.urls', 'favourite'), namespace='favourite')),
]