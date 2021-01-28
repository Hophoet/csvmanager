from django.db import models

#


class Csv(models.Model):
    file1 = models.FileField(upload_to='csvs')
    file2 = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File id:{self.id}'
