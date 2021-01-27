from django.db import models

#
ACTIONS = (
    ('DIF', 'Diference'),
)


class Csv(models.Model):
    file1 = models.FileField(upload_to='csvs')
    file2 = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    actions = models.CharField(
        choices=ACTIONS, max_length=3)

    def __str__(self):
        return f'File id:{self.id}'
