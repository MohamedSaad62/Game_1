from django.db import models

# Create your models here.
class MyTable(models.Model):
    my_string = models.CharField(max_length=255)

    def __str__(self):
        return f"ID: {self.id}, My user is : {self.my_string}"
    class Meta:
        db_table = 'my_table'
        managed = False 