from django.contrib import admin
from . import models
# Register your models here.

# Inline class
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
