# Generated by Django 5.0.2 on 2024-04-14 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbeautystore', '0003_product_duration_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default_images/default_category_image.jpg', upload_to='category_images/'),
        ),
    ]