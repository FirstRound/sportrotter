from rest_framework import generics, filters, permissions

from activities.models import Activity, ActivityRegistration
from activities.serializers import ActivitySerializer, \
    SportrotterUserSerializer, \
    ActivityRegistrationSerializer
from authentication.models import SportrotterUser


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    # anyone can fetch the activity list
    permission_classes = ()

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)

    filter_fields = ('activity_type', 'creation_date', 'rating')
    ordering_fields = ('rating', 'creation_date')

    # add ordering
    # def get_queryset(self):
    #     return super().get_queryset()
    # def filter_queryset(self, queryset):
    #     return queryset.filter(creator=self.request.user)

    #
    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'activity-detail'
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


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

    # def perform_create(self, serializer):
    #     serializer.save(email=serializer.validated_data['username'])


class UserDetail(generics.ListCreateAPIView):
    view_name = 'user-detail'
    queryset = SportrotterUser.objects.all()
    serializer_class = SportrotterUserSerializer


class ActivityRegistrationList(generics.ListAPIView):
    view_name = 'registration-list'
    queryset = ActivityRegistration.objects.all()
    serializer_class = ActivityRegistrationSerializer

    def filter_queryset(self, queryset):
        username = self.request.user.username
        return queryset.filter(users__username__icontains=username)


class ActivityRegistrationDetail(generics.ListCreateAPIView):
    view_name = 'registration-detail'
    queryset = ActivityRegistration.objects.all()
    serializer_class = ActivityRegistrationSerializer


class Me(generics.ListCreateAPIView):
    queryset = SportrotterUser.objects.all()
    serializer_class = SportrotterUserSerializer

    def filter_queryset(self, queryset):
        username = self.request.user.username
        return queryset.filter(username=username)
