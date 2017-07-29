from django.conf import settings
from django.db import models


class Location(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return "lat:{}, lon:{}".format(self.lat, self.lon)


class Activity(models.Model):
    # TODO ask for a list of activity_types
    SURFING = 'SURF'
    ACTIVITY_TYPE_CHOICES = (
        (SURFING, 'Surfing'),
    )
    # TODO add address
    # address = AddressField(related_name="+", blank=True)
    address = models.CharField(max_length=50)
    activity_type = models.CharField(max_length=20,
                                     choices=ACTIVITY_TYPE_CHOICES,
                                     default=SURFING, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()
    background = models.FileField(upload_to='backgrounds')
    logo = models.FileField(upload_to='logos')
    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    rules_of_security = models.CharField(max_length=255)
    description = models.TextField()
    # TODO WTF is this? handle logic
    max_bookings_per_day = models.IntegerField()
    # TODO add available dates

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='created_activities',
                                on_delete=models.CASCADE, default=None)


class ActivityRegistration(models.Model):
    # TODO add payments
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,
                                 related_name='registrations')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='registrations')


class Testimonial(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,
                                 related_name='testimonials')
    issuer = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='testimonials')
    message = models.CharField(max_length=255)
    rating = models.FloatField()


# TODO move messaging to a separate app
class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='outgoing_messages')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name='incoming_messages')


# TODO move payments to a separate app
class Payment(models.Model):
    activity_registration = models.ForeignKey(ActivityRegistration,
                                              on_delete=models.CASCADE,
                                              related_name='payments')
    amount = models.DecimalField(decimal_places=2, max_digits=7)
