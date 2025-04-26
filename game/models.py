from django.db import models

# Create your models here.
class MyTable(models.Model):
    my_number = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id}, My Number: {self.my_number}"
    class Meta:
        db_table = 'myapp_mytable'
        managed = False 