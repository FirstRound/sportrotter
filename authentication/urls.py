from django.conf.urls import url
from rest_framework.authtoken import views

from authentication.views import Logout

urlpatterns = [
    url(r'^login/', views.obtain_auth_token),
    url(r'^logout/', Logout.as_view()),
    # url(r'^register/', Register().as_view())
]
