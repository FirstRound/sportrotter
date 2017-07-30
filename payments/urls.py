from django.conf.urls import url

from payments.views import PaymentDetail

urlpatterns = [
    url(r'^$', PaymentDetail.as_view(), name=PaymentDetail.view_name),
]
