from django.conf.urls import url

from activities import views

urlpatterns = [
    url(r'^activities/$', views.ActivityList.as_view(), name='activity-list'),
    url(r'^activities/(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view(),
        name=views.ActivityDetail.view_name),
    url(r'^users/$', views.UserList.as_view(), name=views.UserList.view_name),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
        name=views.UserDetail.view_name),
    url(r'^me/$', views.Me.as_view()),
    url(r'^activity_registrations/$', views.ActivityRegistrationList.as_view(),
        name=views.ActivityRegistrationList.view_name),
    url(r'^activity_registrations/(?P<pk>[0-9]+)/$',
        views.ActivityRegistrationDetail.as_view(),
        name=views.ActivityRegistrationDetail.view_name),
    # url(r'^activities/(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view())
]
