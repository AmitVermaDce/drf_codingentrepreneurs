from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="detail_view",
        lookup_field = "pk",
    )

class UserPublicSerializers(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

    # def get_other_products(self, obj):
    #     user = obj
    #     my_products_qs = user.products_set.all()
    #     return UserProductInlineSerializer(my_products_qs, many=True, context = self.context).data