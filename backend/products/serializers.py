from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Products
from .validators import validate_title

class ProductsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(
        view_name="detail_view",
        lookup_field = "pk",
    )
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Products
        fields = [
            "pk",
            "url",
            "edit_url", 
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    
    # def validate_title(self, value):
    #     qs = Products.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name...")
    #     return value

    # def create(self, validated_data):
    #     # return Products.objects.create(**validated_data) both are same
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data=validated_data)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title")
    #     return super().update(instance, validated_data)

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

    