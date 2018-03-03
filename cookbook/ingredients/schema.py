import graphene

from graphene_django.types import DjangoObjectType
from cookbook.ingredients.models import Category, Ingredient
from .serializers import CategorySerializer, IngredientSerializer
from graphene_django_extras import DjangoListObjectType, DjangoSerializerType, DjangoSerializerMutation
from graphene_django_extras import DjangoObjectField, DjangoListObjectField, DjangoFilterPaginateListField, DjangoFilterListField, LimitOffsetGraphqlPagination


class CategoryType(DjangoObjectType):
    """Each category"""
    class Meta:
        model = Category
        description = 'Type defination for single category'
        filter_fields = {
            'name': ['icontains', 'iexact']
        }


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        description = 'Ingredient defination'
        filter_fields = {
            'name': ['icontains', 'iexact'],
            'category__name': ['icontains', 'iexact'],
            'category': ['exact']
        }


class Query(object):
    all_categories = DjangoFilterPaginateListField(
        CategoryType, description='all categories query',
        pagination=LimitOffsetGraphqlPagination())
    all_ingredients = DjangoFilterPaginateListField(
        IngredientType, description='all ingredients query',
        pagination=LimitOffsetGraphqlPagination())
    category = DjangoObjectField(
        CategoryType, description='A certain category')
    ingredient = DjangoObjectField(
        IngredientType, description='A certain Ingredient'
    )


class CategorySerializerMutation(DjangoSerializerMutation):
    class Meta:
        description = "Implement writing, updating and deleting of categories"
        serializer_class = CategorySerializer


class IngredientSerializerMutation(DjangoSerializerMutation):
    class Meta:
        description = "Implement writing, updating and deleting of Ingredients"
        serializer_class = IngredientSerializer


class Mutations(graphene.ObjectType):
    category_create = CategorySerializerMutation.CreateField()
    category_delete = CategorySerializerMutation.DeleteField()
    category_update = CategorySerializerMutation.UpdateField()
    ingredient_create = IngredientSerializerMutation.CreateField()
    ingredient_delete = IngredientSerializerMutation.DeleteField()
    ingredient_update = IngredientSerializerMutation.UpdateField()
