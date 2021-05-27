from django.db import models

class Good(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    owner = models.CharField(max_length=255)
    owner_email = models.CharField(max_length=255)

    def __str__(self):
        return self.owner.__str__() + ' ' + self.name.__str__()
