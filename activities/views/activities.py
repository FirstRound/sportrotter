from rest_framework import generics, filters, permissions

from activities.models import Activity
from activities.serializers import ActivitySerializer


class ActivityList(generics.ListCreateAPIView):
    view_name = 'activity-list'
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    # anyone can fetch the activity list
    permission_classes = (permissions.IsAuthenticated,)

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
