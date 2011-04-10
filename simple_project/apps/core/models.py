from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, editable=False)

    def __unicode__(self):
        return self.message