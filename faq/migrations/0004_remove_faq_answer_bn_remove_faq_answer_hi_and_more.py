# Generated by Django 5.1.5 on 2025-02-02 11:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_faq_answer_bn_faq_answer_hi_alter_faq_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answer_bn',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='answer_hi',
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_bn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_hi',
            field=models.TextField(blank=True, null=True),
        ),
    ]
