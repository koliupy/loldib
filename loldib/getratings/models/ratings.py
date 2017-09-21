from django.db import models

class Ratings(models.Model):
    item_ID = models.IntegerField(primary_key=True)
    total_count = models.IntegerField(null=True)
    pick_count = models.IntegerField(null=True)
    win_count = models.IntegerField(null=True)

    class Meta:
        abstract=True
