# coding=utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from mailrobot.models import MailBody


@python_2_unicode_compatible
class Property(models.Model):
    label = models.CharField(max_length=60)

    def __str__(self):
        return self.label


class MailProperty(models.Model):
    mail = models.OneToOneField(MailBody, related_name='mail_property')
    property = models.ForeignKey(Property)
    help_text = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Mail properties"


class TemplateHtmlModel(models.Model):
    name = models.CharField(max_length=64, unique=True)
    label = models.CharField(max_length=120)
    help_text = models.TextField(blank=True, null=True)
    content = models.TextField()
    property = models.ForeignKey(Property, blank=True, null=True)

    def __str__(self):
        return self.name