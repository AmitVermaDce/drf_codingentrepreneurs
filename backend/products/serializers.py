from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(
        view_name="detail_view",
        lookup_field = "pk",
    )
    email = serializers.EmailField(write_only = True)
    class Meta:
        model = Products
        fields = [
            "pk",
            "url",
            "edit_url",
            "email",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    def create(self, validated_data):
        # return Products.objects.create(**validated_data) both are same
        # email = validated_data.pop("email")
        obj = super().create(validated_data=validated_data)
        return obj
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("update_view", kwargs={"pk": obj.pk}, request=request)
        
    
    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Products):
            return None
        return obj.get_discount()

    