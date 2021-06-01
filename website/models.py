from django.db import models

# Create your models here.
class MyProjects(models.Model):
    name = models.CharField(max_length=30)
    language = models.CharField(max_length=10)
    classNum = models.CharField(max_length=10)
    date = models.CharField(max_length=10)

    # Makes shell output more readable
    def __str__(self):
        return f"{self.name} programmed in {self.language} language for {self.classNum} during {self.date}"