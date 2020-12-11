from django.db import models
from django.utils import timezone
import datetime

class Item(models.Model):
    item_label = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    last_done = models.DateTimeField('last done', auto_now=True)

    def __str__(self):
        return self.item_label

    def was_done_recently(self):
        return self.last_done >= timezone.now() - datetime.timedelta(days=1)