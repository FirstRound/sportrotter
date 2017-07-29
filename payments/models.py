from django.db import models


class Payment(models.Model):
    class PaymentStatus:
        NOT_DONE = 'NOT_DONE'
        WAITING_FOR_CONFIRMATION = 'WAITING_FOR_CONFIRMATION'
        SUCCESSFUL = 'SUCCESSFUL'
        PAYMENT_STATUS_CHOICES = (
            (NOT_DONE, 'Not done'),
            (WAITING_FOR_CONFIRMATION, 'Waiting for confirmation'),
            (SUCCESSFUL, 'Successful')
        )

    amount = models.DecimalField(decimal_places=2, max_digits=7)
    status = models.CharField(max_length=20,
                              choices=PaymentStatus.PAYMENT_STATUS_CHOICES,
                              default=PaymentStatus.NOT_DONE, blank=True)
