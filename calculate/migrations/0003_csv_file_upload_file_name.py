# Generated by Django 4.0.5 on 2022-11-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0002_alter_csv_file_upload_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv_file_upload',
            name='file_name',
            field=models.CharField(default=None, max_length=15),
        ),
    ]