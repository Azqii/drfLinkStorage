from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    """The ModelSerializer for Link model"""
    id = serializers.ReadOnlyField()
    added_by = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = Link
        fields = "__all__"
