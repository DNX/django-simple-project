from django.contrib import admin
from core.models import *

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)