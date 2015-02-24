# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TemplateHtmlModel.help_text'
        db.add_column(u'duck_utils_templatehtmlmodel', 'help_text',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'TemplateHtmlModel.property'
        db.alter_column(u'duck_utils_templatehtmlmodel', 'property_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duck_utils.Property'], null=True))

    def backwards(self, orm):
        # Deleting field 'TemplateHtmlModel.help_text'
        db.delete_column(u'duck_utils_templatehtmlmodel', 'help_text')


        # User chose to not deal with backwards NULL issues for 'TemplateHtmlModel.property'
        raise RuntimeError("Cannot reverse this migration. 'TemplateHtmlModel.property' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TemplateHtmlModel.property'
        db.alter_column(u'duck_utils_templatehtmlmodel', 'property_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duck_utils.Property']))

    models = {
        u'duck_utils.mailproperty': {
            'Meta': {'object_name': 'MailProperty'},
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'mail_property'", 'unique': 'True', 'to': u"orm['mailrobot.MailBody']"}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['duck_utils.Property']"})
        },
        u'duck_utils.property': {
            'Meta': {'object_name': 'Property'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'duck_utils.templatehtmlmodel': {
            'Meta': {'object_name': 'TemplateHtmlModel'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'help_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['duck_utils.Property']", 'null': 'True', 'blank': 'True'})
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