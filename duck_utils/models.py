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
    help_text = models.TextField()

    class Meta:
        verbose_name_plural = "Mail properties"
