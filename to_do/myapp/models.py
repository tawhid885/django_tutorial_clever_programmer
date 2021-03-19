from django.db import models

class todo(models.Model):
    added_date=models.DateTimeField(auto_now=True)
    text=models.CharField(max_length=500)

    def __str__(self):
        return self.text
