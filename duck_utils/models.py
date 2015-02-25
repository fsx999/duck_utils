# coding=utf-8
import tempfile
from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import render_to_string
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe
from mailrobot.models import MailBody
from wkhtmltopdf import wkhtmltopdf


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
        template = render_to_string(self.name, context)
        f = tempfile.NamedTemporaryFile(mode='w+b', bufsize=-1,
                                        suffix='.html', prefix='tmp', dir=None,
                                        delete=True)
        f.write(template)
        f.flush()
        pdf_file = wkhtmltopdf([f.name], output)
        f.close()
        return pdf_file

    def get_preview_button(self):
        url = reverse('preview_html', kwargs={'pk': self.pk})
        return mark_safe('<a href="{}"><input type="button" value="Preview" /></a>'.format(url))
    get_preview_button.short_description = "Preview"


