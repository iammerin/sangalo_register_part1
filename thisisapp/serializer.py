from rest_framework import serializers
from .models import *


class SuburbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suburb1
        fields = ['id', 'suburb_name', ]
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    suburbs = SuburbSerializer(many=True, read_only=True)

    class Meta:
        model = Post1
        fields = ['id', 'post_code', 'suburbs', ]
        read_only_fields = ('id',)


class StateSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = State1
        fields = ['id', 'state_name', 'posts', ]
        read_only_fields = ('id',)


class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True, read_only=True)

    # posts = PostSerializer(many=True)
    # suburbs = SuburbSerializer(many=True)

    class Meta:
        model = Country1
        # fields = '__all__'
        fields = ['id', 'country_name', 'country_code', 'states', ]
        # read_only_fields = ('id',)

    # def get_states(self, obj):
    #     state_name = self.context['request'].query_params.get('state_name', None)
    #     states = obj.states.filter(state_name=state_name)
    #     return CountrySerializer(states, many=True).data


# class NumberSerializer(serializers.Serializer):
#     number = serializers.CharField()
#     # state_name = serializers.CharField()
#     # postal_code = serializers.CharField()


# class ThisisitSerializer(serializers.Serializer):
#     # number = serializers.CharField()
#     state_name = serializers.CharField()


# class SuburbNameSerializer(serializers.Serializer):
#     # number = serializers.CharField()
#     state_name = serializers.CharField()
#     # postal_code = serializers.CharField()