from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    upload_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title