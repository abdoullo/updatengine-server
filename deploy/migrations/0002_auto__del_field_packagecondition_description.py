# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'packagecondition.description'
        db.delete_column('deploy_packagecondition', 'description')


    def backwards(self, orm):
        # Adding field 'packagecondition.description'
        db.add_column('deploy_packagecondition', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)


    models = {
        'deploy.package': {
            'Meta': {'object_name': 'package'},
            'command': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'conditions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['deploy.packagecondition']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'packagesum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        'deploy.packagecondition': {
            'Meta': {'object_name': 'packagecondition'},
            'depends': ('django.db.models.fields.CharField', [], {'default': "'installed'", 'max_length': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'softwarename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'softwareversion': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'deploy.packagehistory': {
            'Meta': {'object_name': 'packagehistory'},
            'command': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.machine']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['deploy.package']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'packagesum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Programmed'", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'deploy.packageprofile': {
            'Meta': {'object_name': 'packageprofile'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'packages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['deploy.package']", 'null': 'True', 'blank': 'True'})
        },
        'inventory.entity': {
            'Meta': {'object_name': 'entity'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['inventory.entity']"})
        },
        'inventory.machine': {
            'Meta': {'object_name': 'machine'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.entity']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastsave': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'netsum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'ossum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'packageprofile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['deploy.packageprofile']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'packages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['deploy.package']", 'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'softsum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'typemachine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.typemachine']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inventory.typemachine': {
            'Meta': {'object_name': 'typemachine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['deploy']