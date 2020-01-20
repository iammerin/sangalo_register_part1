from rest_framework import serializers
from .models import *


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name', ]
        read_only_fields = ('id',)


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'post_code', ]
#         read_only_fields = ('id',)


class SuburbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suburb
        fields = ['id', 'suburb_name', ]
        read_only_fields = ('id',)


class CountrySerializer(serializers.ModelSerializer):
    # states = StateSerializer(many=True)

    # posts = PostSerializer(many=True)
    # suburbs = SuburbSerializer(many=True)

    class Meta:
        model = Country
        fields = ['id', 'country_name', 'country_code', ]
        read_only_fields = ('id',)

    # def get_states(self, obj):
    #     state_name = self.context['request'].query_params.get('state_name', None)
    #     states = obj.states.filter(state_name=state_name)
    #     return CountrySerializer(states, many=True).data


class NumberSerializer(serializers.Serializer):
    number = serializers.CharField()
    # state_name = serializers.CharField()
    # postal_code = serializers.CharField()


# class ThisisitSerializer(serializers.Serializer):
#     # number = serializers.CharField()
#     state_name = serializers.CharField()


class SuburbNameSerializer(serializers.Serializer):
    # number = serializers.CharField()
    state_name = serializers.CharField()
    # postal_code = serializers.CharField()