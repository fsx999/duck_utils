# coding=utf-8
import tempfile
from django.template.loader import render_to_string
from django.utils.encoding import smart_text
from wkhtmltopdf import wkhtmltopdf, make_absolute_paths

__author__ = 'paulguichon'
from django.conf import settings


def email_ied(individu):
    return str(individu.cod_etu) + '@foad.iedparis8.net'


def get_recipients(individu, cod_anu):
    if settings.DEBUG:
        recipients = (settings.EMAIL_DEV, )
    else:
        email = individu.get_email(cod_anu)
        if email:
            recipients = (individu.get_email(cod_anu), email_ied(individu))
        else:
            recipients = (email_ied(individu), )
    return recipients

def make_pdf(name, context, output=None):
    template = render_to_string(name, context)
    content = smart_text(template)
    content = make_absolute_paths(content)
    f = tempfile.NamedTemporaryFile(mode='w+b', bufsize=-1,
                                    suffix='.html', prefix='tmp', dir=None,
                                    delete=True)
    f.write(content)
    f.flush()
    pdf_file = wkhtmltopdf([f.name], output)
    f.close()
    return pdf_file
