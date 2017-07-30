from django.http import JsonResponse
from django.views import View
from rest_framework import generics, filters, permissions, status
from rest_framework.decorators import detail_route, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from activities import utils
from activities.models import Activity
from activities.serializers import ActivitySerializer
from authentication.models import SportrotterUser
from authentication.serializers import SportrotterUserSerializer


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


class FileUpload(View):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        ext = uploaded_file.name.split('.')[-1]
        file_path, file_url = utils.make_new_path(ext=ext)

        with open(file_path, 'wb') as runner_file:
            for chunk in uploaded_file.chunks():
                runner_file.write(chunk)
        return JsonResponse(status=status.HTTP_201_CREATED,
                            data={'url': file_url})


class UserList(generics.ListCreateAPIView):
    view_name = 'user-list'
    queryset = SportrotterUser.objects.all()
    serializer_class = SportrotterUserSerializer
    permission_classes = (UserViewPermissions,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('username', 'email')

    # def perform_create(self, serializer):
    #     serializer.save(email=serializer.validated_data['username'])


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    view_name = 'user-detail'
    queryset = SportrotterUser.objects.all()
    serializer_class = SportrotterUserSerializer


# class ActivityRegistrationList(generics.ListAPIView):
#     view_name = 'registration-list'
#     queryset = ActivityRegistration.objects.all()
#     serializer_class = ActivityRegistrationSerializer
#
#     def filter_queryset(self, queryset):
#         username = self.request.user.username
#         return queryset.filter(users__username__icontains=username)
#
#
# class ActivityRegistrationDetail(generics.ListCreateAPIView):
#     view_name = 'registration-detail'
#     queryset = ActivityRegistration.objects.all()
#     serializer_class = ActivityRegistrationSerializer


class Me(generics.RetrieveAPIView):
    queryset = SportrotterUser.objects.all()
    serializer_class = SportrotterUserSerializer

    def filter_queryset(self, queryset):
        username = self.request.user.username
        return queryset.filter(username=username)
