from django.db import models

class Message(models.Model):
    message = models.TextField()

    def __unicode__(self):
        return self.message