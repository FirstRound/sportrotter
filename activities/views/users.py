from rest_framework import generics, filters, permissions

from authentication.models import SportrotterUser
from authentication.serializers import SportrotterUserSerializer


class UserViewPermissions(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return super().has_permission(request, view)


class UserList(generics.ListCreateAPIView):
    view_name = 'user-list'
    queryset = SportrotterUser.objects.all()
    serializer_class = SportrotterUserSerializer
    permission_classes = (UserViewPermissions,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('username', 'email')


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'user-detail'
    queryset = SportrotterUser.objects.all()
    serializer_class = SportrotterUserSerializer
