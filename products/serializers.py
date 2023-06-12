from rest_framework import serializers

from .models import Category, Tag, Product


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["url", "name"]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["url", "name"]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ["user", "updated_at"]


class ProductCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ["user", "updated_at"]


class TagProductListSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedIdentityField(view_name="product_by_tag-detail")

    class Meta:
        model = Tag
        fields = ["name", "products"]


class CategoryProductListSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedIdentityField(view_name="product_by_category-detail")

    class Meta:
        model = Category
        fields = ["name", "products"]
