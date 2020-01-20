from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Country1
from . serializer import *
from rest_framework import generics


# class NewStateList(generics.ListAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer


# class StateList(APIView):
#     def post(self, request):
#         serializer = NumberSerializer(data=request.data)
#
#         if serializer.is_valid():
#             data = serializer.data
#             ccode = data['number']
#             cid = Country.objects.filter(country_code=ccode).values('pk')
#             for x in cid:
#                 couid = x['pk']
#                 dict = {}
#                 state = State.objects.filter(country=couid).values()
#                 # serializer = StateSerializer(state, many=True)
#                 # print(serializer)
#                 dict['details'] = state
#                 return Response(dict)
#             return Response({'error': serializer.errors})


# class PostalCode(APIView):
#     def post(self, request):
#         serializer = SuburbNameSerializer(data=request.data)
#
#         if serializer.is_valid():
#             data = serializer.data
#             ccode = data['state_name']
#             cid = State.objects.filter(state_name=ccode).values('pk')
#             for x in cid:
#                 couid = x['pk']
#                 dict = {}
#                 state = Suburb.objects.filter(state=couid).values()
#                 # serializer = StateSerializer(state, many=True)
#                 # print(serializer)
#                 dict['details'] = state
#                 print(dict)
#                 return Response(dict)
#             return Response(serializer.error)


# class SuburbNameList(APIView):
#     def post(self, request):
#         serializer = SuburbNameSerializer(data=request.data)
#
#         if serializer.is_valid():
#             data = serializer.data
#             ccode = data['postal_code']
#             cid = Post.objects.filter(post_code=ccode).values('pk')
#             for x in cid:
#                 couid = x['pk']
#                 dict = {}
#                 state = Suburb.objects.filter(post=couid).values()
#                 # serializer = StateSerializer(state, many=True)
#                 # print(serializer)
#                 dict['details'] = state
#                 print(dict)
#                 return Response(dict)
#             return Response(serializer.error)


# class InformationList(APIView):
#     def get(self, request):
#         dict = {}
#         state = Country.objects.all()
#         serializer = CountrySerializer(state, many=True)
#         state_name = self.request.query_params.get('state_name', None)
#         if state_name is not None:
#             state = queryset.filter(state__statename)
#         dict['details'] = serializer.data
#         return Response(dict)

# class InformationList(APIView):
#
#     def get(self, request):
#         dict = {}
#         state = Country.objects.all()
#         serializer = CountrySerializer(state, many=True)
#         print(serializer)
#         dict['details'] = serializer.data
#         return Response(dict)

class InformationList(APIView):

    def get(self,request):
        country = State1.objects.get(id=1)
        serializer = StateSerializer(instance=country)
        return Response(serializer.data)


class InformationList1(APIView):

    def get(self,request):
        country = Country1.objects.get(id=2)
        serializer = CountrySerializer(instance=country)
        return Response(serializer.data)

    # def get(self, request):
    #     dict = {}
    #     dict2 = {}
    #     country = Country.objects.all()
    #     state = State1.objects.all()
    #     serializer1 = CountrySerializer(country, many=True)
    #     serializer2 = StateSerializer(state, many=True)
    #     # print(serializer)
    #     dict['details'] = serializer1.data
    #     dict['details'] = {'states': serializer2.data}
    #     return Response(dict)


# class AgainList(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = CountrySerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             state = S
#             return Response({
#
#             })

# class PostList(APIView):
#     def get(self, request):
#         dict = {}
#         post = Post.objects.all()
#         serializer = PostSerializer(post, many=True)
#         dict['details'] = serializer.data
#         return Response(dict)
#
#
# class SuburbList(APIView):
#     def get(self, request):
#         dict = {}
#         suburb = Suburb.objects.all()
#         serializer = SuburbSerializer(suburb, many=True)
#         dict['details'] = serializer.data
#         return Response(dict)


