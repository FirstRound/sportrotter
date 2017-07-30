from django.conf.urls import url

from payments.views import PaymentDetail

app_name = 'payments'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', PaymentDetail.as_view(),
        name=PaymentDetail.view_name),
]
