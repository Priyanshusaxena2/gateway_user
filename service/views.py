from rest_framework import viewsets
from rest_framework.response import Response

from service.models import User, Address
from service.utils import validate_request
from service.serializers import UserSerializer, AddressSerializer, FetchAddressSerializer


class UserViewSet(viewsets.ViewSet):

    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.validated_data
        else:
            response = serializer.errors
        return Response(response)

    @validate_request(params_fields=['fields', 'id'])
    def get_users(self, request):
        fields = request.GET.get('fields').split(',')
        ids = request.GET.get('id').split(',')
        users = User.objects.filter(pk__in=ids)
        serializer = UserSerializer(users, fields=fields, many=True)
        return Response(serializer.data)


class AddressViewSet(viewsets.ViewSet):

    def create_address(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
        else:
            response = serializer.errors
        return Response(response)

    @validate_request(params_fields=['users', 'type'])
    def get_addresses(self, request):
        users = request.GET.get('users').split(',')
        type = request.GET.get('type').split(',')
        addresses = Address.objects.filter(user__in=users, type__in=type)
        serializer = FetchAddressSerializer(addresses, many=True)
        return Response(serializer.data)