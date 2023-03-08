from rest_framework import serializers

from .models import Link
from .services import is_url


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    """The ModelSerializer for the Link model"""
    id = serializers.ReadOnlyField()

    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = ("added_by",)

    # Should've used URLField in model here, made just to practice DRF
    def validate_link_url(self, value):
        """Checks if the provided link_url is an actual url"""
        if not is_url(value):
            raise serializers.ValidationError("Enter a valid url for link")
        return value
