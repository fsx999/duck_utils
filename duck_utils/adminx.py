from ckeditor.widgets import CKEditorWidget
from mailrobot.models import MailBody, Mail, Address, Signature
import reversion
from wkhtmltopdf.views import PDFTemplateView
from duck_utils.models import MailProperty, Property, TemplateHtmlModel
import xadmin
from xadmin.views import filter_hook
from xadmin.layout import Layout, Fieldset, Container, Col


class MailPropertyInline(object):
    model = MailProperty
    can_delete = False
    extra = 1
    max_num = 1
    readonly_fields = ['property', 'help_text']
    fields = ['property',
              'help_text']

    @filter_hook
    def get_readonly_fields(self):
        if self.user.is_superuser:
            return []
        else:
            return self.readonly_fields


class MailBodyAdmin(object):
    inlines = [MailPropertyInline]

    readonly_fields = ['name']
    form_layout = Layout(Container(Col('full',
                                       Fieldset('',
                                                'name',
                                                'subject',
                                                'body'
                                                , css_class="unsort no_title"), horizontal=True, span=12)
                                   ))

    @filter_hook
    def get_list_queryset(self):
        query = super(MailBodyAdmin, self).get_list_queryset()
        if not self.user.is_superuser:
            query = query.filter(mail_property__property__in=self.user.setting_user.property.all())
        return query


    @filter_hook
    def get_readonly_fields(self):
        if self.user.is_superuser:
            return []
        else:
            return self.readonly_fields


class TemplateHtmlModelAdmin(object):
    reversion_enable = True
    readonly_fields = ['get_preview_button']

    @filter_hook
    def get_field_attrs(self, db_field, **kwargs):
        if db_field.name == 'content':
            return {'widget': CKEditorWidget}
        return super(TemplateHtmlModelAdmin, self).get_field_attrs(db_field, **kwargs)


class PreviewHtmlModelView(PDFTemplateView):
    filename = "PreviewHtml_{}_{}.pdf"
    template_name = ""

    def get_template_names(self):
        pk = self.kwargs.get('pk', None)
        res = TemplateHtmlModel.objects.get(pk=pk)
        return res.name

    def get_filename(self):
        return self.filename.format(self.kwargs.get('pk', 'Anomalie'), self.kwargs.get('session', 'Anomalie'))

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        res = TemplateHtmlModel.objects.get(pk=pk)
        context = super(PreviewHtmlModelView, self).get_context_data(**kwargs)
        c = res.get_context_test()
        context.update(c)

        return context

xadmin.site.register(MailBody, MailBodyAdmin)
xadmin.site.register(Mail)
xadmin.site.register(Address)
xadmin.site.register(Signature)
xadmin.site.register(Property)
xadmin.site.register(TemplateHtmlModel, TemplateHtmlModelAdmin)
xadmin.plugins.xversion.register_models()