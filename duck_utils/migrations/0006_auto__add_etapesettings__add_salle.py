# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EtapeSettings'
        db.create_table(u'duck_utils_etapesettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'duck_utils', ['EtapeSettings'])

        # Adding model 'Salle'
        db.create_table(u'duck_utils_salle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'duck_utils', ['Salle'])


    def backwards(self, orm):
        # Deleting model 'EtapeSettings'
        db.delete_table(u'duck_utils_etapesettings')

        # Deleting model 'Salle'
        db.delete_table(u'duck_utils_salle')


    models = {
        u'duck_utils.etapesettings': {
            'Meta': {'object_name': 'EtapeSettings'},
            'contact_info': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
        u'duck_utils.salle': {
            'Meta': {'object_name': 'Salle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'duck_utils.templatehtmlmodel': {
            'Meta': {'object_name': 'TemplateHtmlModel'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'context_test': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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