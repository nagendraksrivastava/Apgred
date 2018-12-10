# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class NotificationDetails(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255, blank=True)
    priority = models.CharField(max_length=255, default='DEFAULT')
    category = models.CharField(max_length=255, default='MESSAGE')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class NotificationModel(models.Model):
    user = models.OneToOneField(User, blank=False, unique=True)
    details = models.ForeignKey(NotificationDetails)
    delivered = models.BooleanField(default=False)
    clicked = models.BooleanField(default=False)
    discarded = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
