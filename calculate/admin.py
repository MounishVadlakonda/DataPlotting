

# Register your models here.
from django.contrib import admin

from .models import csv_file_upload  # import your model

admin.site.register(csv_file_upload) # actual registration