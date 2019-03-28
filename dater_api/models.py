from django.contrib.auth.models import User, Group

from django.db import models

class ProviderClient(models.Model):
    name = models.CharField(max_length=255)

class AvailableSlot(models.Model):
    client = models.ForeignKey(ProviderClient, on_delete=models.CASCADE)
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()

class SlotType(models.Model):
    client = models.ForeignKey(ProviderClient, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    length = models.IntegerField()

class BookedSlot(models.Model):
    slot = models.ForeignKey(AvailableSlot, on_delete=models.CASCADE)
    slot_type = models.ForeignKey(SlotType, on_delete=models.CASCADE)
    from_time = models.TimeField()
    to_time = models.TimeField()
    bestaetigt = models.BooleanField(default=False)
    created_at = models.DateTimeField()

class ProviderData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client = models.ForeignKey(ProviderClient, on_delete=models.CASCADE)

class ConsumerData(models.Model):
    """ Consumers can be identified in various ways:
      * e-mail address (User.email)
      * phone number
      * when not registered yet: session key

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=64)
    session_key =  models.CharField(max_length=255)

