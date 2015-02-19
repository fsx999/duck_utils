# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MailProperty.help_text'
        db.add_column(u'duck_utils_mailproperty', 'help_text',
                      self.gf('django.db.models.fields.TextField')(default='help text'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MailProperty.help_text'
        db.delete_column(u'duck_utils_mailproperty', 'help_text')


    models = {
        u'duck_utils.mailproperty': {
            'Meta': {'object_name': 'MailProperty'},
            'help_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'mail_property'", 'unique': 'True', 'to': u"orm['mailrobot.MailBody']"}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['duck_utils.Property']"})
        },
        u'duck_utils.property': {
            'Meta': {'object_name': 'Property'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'mailrobot.mailbody': {
            'Meta': {'object_name': 'MailBody'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '66'})
        }
    }

    complete_apps = ['duck_utils']