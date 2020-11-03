from rest_framework import serializers

from common.models import User


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email']


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    created_by = UserNestedSerializer(read_only=True)
    modified_by = UserNestedSerializer(read_only=True)

    def __init__(self, *args, **kwargs):
        super(BaseSerializer, self).__init__(*args, **kwargs)
        self.add_timestamp_fields()

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['modified_by'] = self.context['request'].user
        return super(BaseSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['modified_by'] = self.context['request'].user
        return super(BaseSerializer, self).update(instance, validated_data)


