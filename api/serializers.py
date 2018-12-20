from rest_framework import serializers
from items.models import Item ,FavoriteItem
from django.contrib.auth.models import User

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['item', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ItemListSerializer(serializers.ModelSerializer):
    itemn = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = "item-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    added_by = UserSerializer()
   
    class Meta:
        model = Item
        fields = ['name','image', 'description','detail' ,'added_by' , 'itemn']
    def get_itemn(self, obj):
        return obj.favoriteitem_set.count()


class DetailListSerializer(serializers.ModelSerializer):
    iteml = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['name','image', 'description', 'iteml']

    def get_iteml(self, obj):
        return ItemListSerializer(obj.iteml_set.all(),many=True).data

