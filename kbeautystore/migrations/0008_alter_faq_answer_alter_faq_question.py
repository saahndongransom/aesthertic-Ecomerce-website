# Generated by Django 5.0.2 on 2024-04-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbeautystore', '0007_faq_delete_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(),
        ),
    ]
