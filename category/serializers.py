from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        exclude = ('sub_category', )


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.category_set.exists():
            representation['child'] = CategorySerializer(
                instance.category_set.all(), many=True
            ).data
        return representation
