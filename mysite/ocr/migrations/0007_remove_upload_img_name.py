# Generated by Django 4.1.3 on 2023-07-03 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0006_rename_text_name_upload_img_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='img_name',
        ),
    ]
