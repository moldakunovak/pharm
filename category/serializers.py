from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        # exclude = ('sub_category', )

    # def to_representation(self, instance):
        # representation = super().to_representation(instance)
        # if instance.sub_categoryies.exists():
        #     representation['child'] = CategorySerializer(
        #         instance.sub_categoryies.all(), many=True
        #     ).data
        # return representation
