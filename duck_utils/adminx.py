from mailrobot.models import MailBody, Mail, Address, Signature
from duck_utils.models import MailProperty, Property
import xadmin
from xadmin.views import filter_hook


class MailPropertyInline(object):
    model = MailProperty
    can_delete = False
    extra = 1
    max_num = 1
    readonly_fields = ['property', 'help_text']
    fields = ['property',
              'help_text',]
    @filter_hook
    def get_readonly_fields(self):
        if self.user.is_superuser:
            return []
        else:
            return self.readonly_fields



class MailBodyAdmin(object):
    inlines = [MailPropertyInline]
    @filter_hook
    def get_list_queryset(self):
        query = super(MailBodyAdmin, self).get_list_queryset()
        if not self.user.is_superuser:
            query = query.filter(mail_property__property__in=self.user.setting_user.property.all())
        return query

xadmin.site.register(MailBody, MailBodyAdmin)
xadmin.site.register(Mail)
xadmin.site.register(Address)
xadmin.site.register(Signature)
xadmin.site.register(Property)
