from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader
from duck_utils.models import TemplateHtmlModel


class Loader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        try:
            return TemplateHtmlModel.objects.get(name=template_name).content, template_name

        except TemplateHtmlModel.DoesNotExist:
            raise TemplateDoesNotExist(template_name)