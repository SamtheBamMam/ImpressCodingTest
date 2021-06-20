from django.db import models

# Create your models here.

'''Model to store the number of calls to each type of button per person and 
    update it on every new call.'''


class ButtonCall(models.Model):
    user = models.CharField(max_length=200)
    fat_count = models.IntegerField(default=0)
    stupid_count = models.IntegerField(default=0)
    dumb_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

