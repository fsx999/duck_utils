# coding=utf-8
import tempfile
from PyPDF2 import PdfFileWriter, PdfFileReader
import cStringIO
from django.template.loader import render_to_string
from django.utils.encoding import smart_text
from wkhtmltopdf import wkhtmltopdf, make_absolute_paths
from wkhtmltopdf.views import PDFTemplateResponse
from tempfile import NamedTemporaryFile
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

def render_to_temporary_file(template_name, context,  mode='w+b', bufsize=-1,
                                 suffix='.html', prefix='tmp', dir=None,
                                 delete=True):
        template = render_to_string(template_name, context)
        content = smart_text(template)
        content = make_absolute_paths(content)

        try:
            # Python3 has 'buffering' arg instead of 'bufsize'
            tempfile = NamedTemporaryFile(mode=mode, buffering=bufsize,
                                          suffix=suffix, prefix=prefix,
                                          dir=dir, delete=delete)
        except TypeError:
            tempfile = NamedTemporaryFile(mode=mode, bufsize=bufsize,
                                          suffix=suffix, prefix=prefix,
                                          dir=dir, delete=delete)

        try:
            tempfile.write(content.encode('utf-8'))
            tempfile.flush()
            return tempfile
        except:
            # Clean-up tempfile if an Exception is raised.
            tempfile.close()
            raise

def make_pdf(name, context, header_filename=None, footer_filename=None, output=None):
    cmd_options = {}
    if header_filename is not None:
        header = render_to_temporary_file(header_filename, context)
        cmd_options['header_html'] = header.name
    if footer_filename is not None:
        footer = render_to_temporary_file(footer_filename, context)
        cmd_options['footer_html'] = footer.name
    f = render_to_temporary_file(name, context)
    pdf_file = wkhtmltopdf([f.name], output, **cmd_options)
    f.close()
    if footer_filename:
        footer.close()
    if header_filename:
        header.close()
    return pdf_file


def append_pdf(input, output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]


class MultiPDFTemplateResponse(PDFTemplateResponse):
    templates_files = []
    files = []

    @property
    def rendered_content(self):
        output = PdfFileWriter()

        for name in self.templates_name:
            self.template_name = name
            buffer = cStringIO.StringIO()
            buffer.write(super(MultiPDFTemplateResponse, self).rendered_content)
            append_pdf(PdfFileReader(buffer), output)
        for file in self.files:
            append_pdf(PdfFileReader(file), output)
        o = cStringIO.StringIO()
        output.write(o)
        return o.getvalue()


def make_multi_pdf(context, templates, files=[]):
    output = PdfFileWriter()

    for template in templates:
        buffer = cStringIO.StringIO()
        buffer.write(make_pdf(template['name'], context, template.get('header', None), template.get('footer', None)), )
        append_pdf(PdfFileReader(buffer), output)
    for file in files:
        append_pdf(PdfFileReader(file), output)
    o = cStringIO.StringIO()
    output.write(o)
    return o.getvalue()


def remove_page_pdf(file, nb=1):
    """
    retourne un pdf sans les nb pages
    """
    result = cStringIO.StringIO()
    output = PdfFileWriter()
    input1 = PdfFileReader(file)
    for x in range(nb, input1.getNumPages()):
        output.addPage(input1.getPage(x))
    output.write(result)

    return result

def num_page(pdf):
    return PdfFileReader(pdf).getNumPages()