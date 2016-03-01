# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailrobot', '__first__'),
        ('django_apogee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtapeSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_anu', models.IntegerField()),
                ('contact_info', models.TextField()),
                ('etape', models.ForeignKey(to='django_apogee.Etape')),
            ],
            options={
                'verbose_name_plural': 'etape settings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('help_text', models.TextField(blank=True)),
                ('mail', models.OneToOneField(related_name='mail_property', to='mailrobot.MailBody')),
            ],
            options={
                'verbose_name_plural': 'Mail properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateHtmlModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('label', models.CharField(max_length=120)),
                ('help_text', models.TextField(null=True, blank=True)),
                ('content', models.TextField()),
                ('context_test', models.TextField(null=True, blank=True)),
                ('property', models.ForeignKey(blank=True, to='duck_utils.Property', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mailproperty',
            name='property',
            field=models.ForeignKey(to='duck_utils.Property'),
            preserve_default=True,
        ),
    ]
