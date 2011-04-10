from django.contrib import admin
from core.models import *

class MessageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """
        Automatically fill in the user field on creation.
        """
        if not change:
            obj.user = request.user
        super(self.__class__, self).save_model(request, obj, form, change)

admin.site.register(Message, MessageAdmin)