# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe
from mailrobot.models import MailBody
from django_apogee.models import Etape
from duck_utils.utils import make_pdf


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

    context_test = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_context_test(self):
        return eval(self.context_test)

    def get_pdf_file(self, context, output=None):
        return make_pdf(self.name, context, output)

    def get_preview_button(self):
        url = reverse('preview_html', kwargs={'pk': self.pk})
        return mark_safe('<a href="{}"><input type="button" value="Preview" /></a>'.format(url))
    get_preview_button.short_description = "Preview"


class EtapeSettings(models.Model):
    class Meta:
        verbose_name_plural = "etape settings"

    etape = models.ForeignKey(Etape)
    cod_anu = models.IntegerField()
    contact_info = models.TextField() # Coordonnées du ou des responsables de l'étape.

    def __str__(self):
        return "{} {}".format(self.etape, self.cod_anu)

class Salle(models.Model):
    label = models.CharField(max_length=120)

    def __str__(self):
        return self.label