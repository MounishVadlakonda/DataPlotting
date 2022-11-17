from django.db import models

# Create your models here.
class csv_file_upload(models.Model):
    csv_file = models.FileField(upload_to = 'static/datasets/')

    def __str__(self):
        return str(self.csv_file)

    class Meta:
        db_table = 'datasets'
        # Add verbose name
        verbose_name = 'dataset'