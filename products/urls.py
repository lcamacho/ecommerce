from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from products import views

router = routers.DefaultRouter()
router.register(r"product", views.ProductViewSet)
router.register(r"product_by_date", views.ProductByDateView, basename="product_by_date")
router.register(r"product_by_tag", views.ProductByTagView, basename="product_by_tag")
router.register(r"product_by_category", views.ProductByCategoryView, basename="product_by_category")
router.register(
    r"product_by_title", views.ProductByTitleView, basename="product_by_title"
)
router.register(r"tag", views.TagViewSet)
router.register(r"category", views.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
