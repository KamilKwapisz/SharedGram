from rest_framework import serializers

from .graph_models import Comment


class CommentSerializer(serializers.Serializer):
    uid = serializers.CharField(read_only=True)
    author = serializers.CharField()
    text = serializers.CharField()
    date = serializers.DateTimeField()
    # post = PostSerializer()
    # liked_by = UserSerializer(many=True)
    # commented_by = UserSerializer(many=True)

    def create(self, validated_data):
        return Comment(uid=None, **validated_data)

    def update(self, instance, validated_data):
        return Comment(uid=None, **validated_data)
