from django.conf.urls import url

from activities.views.activities import ActivityList, ActivityDetail
from activities.views.misc import FileUploadView, Me
from activities.views.registrations import CreateBooking, BookingDetail
from activities.views.users import UserList, UserDetail

urlpatterns = [
    url(r'^activities/$', ActivityList.as_view(), name=ActivityList.view_name),
    url(r'^activities/(?P<pk>[0-9]+)/$', ActivityDetail.as_view(),
        name=ActivityDetail.view_name),

    url(r'^users/$', UserList.as_view(), name=UserList.view_name),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(),
        name=UserDetail.view_name),
    url(r'^me/$', Me.as_view(), name=Me.view_name),

    url(r'^upload/$', FileUploadView.as_view(), name=FileUploadView.view_name),

    url(r'^bookings/$', CreateBooking.as_view(), name=CreateBooking.view_name),
    url(r'^bookings/(?P<pk>[0-9]+)/$', BookingDetail.as_view(),
        name=BookingDetail.view_name),
]
