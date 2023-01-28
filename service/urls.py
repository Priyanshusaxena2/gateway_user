from django.urls import path
from .views import UserViewSet,AddressViewSet

urlpatterns = [
    path('user/create', UserViewSet.as_view({
        'post': 'create_user'
    }), name='create_user'),
    path('user/', UserViewSet.as_view({
        'get': 'get_users'
    }), name='get_users'),
    path('address/create', AddressViewSet.as_view({
        'post': 'create_address'
    }), name='create_address'),
    path('address/', AddressViewSet.as_view({
        'get': 'get_addresses'
    }), name='get_addresses')


]
