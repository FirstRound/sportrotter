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
    title = models.CharField(max_length=50, blank=True)
    rules_of_security = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    # TODO WTF is this? handle logic
    max_bookings_per_day = models.IntegerField(default=1, blank=True)
    # TODO add available dates

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='created_activities',
                                on_delete=models.CASCADE, default=None)


class Booking(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    date = models.DateField()


class ClientRegistration(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='registrations')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE,
                                related_name='registrations')
    payment = models.OneToOneField('payments.Payment', on_delete=models.CASCADE)


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
