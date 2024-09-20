# Question 3: By default do django signals run in the same database transaction as the caller?

# Answer:
# Django signals do not run in the same database transaction as the caller by default
# Due to this, the signal receiver functions execute within the same thread as the code that triggered the signal

#Example is provided below
import django
from django.db import models, transaction
from django.dispatch import Signal

django.setup()

signal = Signal()

class model(models.Model):
    name = models.CharField(max_length=100)

def receiver(sender, instance, **kwargs):
    with transaction.atomic():
        model.objects.create(name="Signal receiver")

def trigger_signal():
    with transaction.atomic():
        model.objects.create(name="Caller")
        signal.send(sender=None, instance=model())

trigger_signal()