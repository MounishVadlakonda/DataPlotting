# Generated by Django 4.0.5 on 2022-11-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0003_csv_file_upload_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_file_upload',
            name='file_name',
            field=models.CharField(max_length=200),
        ),
    ]
