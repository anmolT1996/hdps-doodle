from django.db import models

# Create your models here
class Student(models.Model):
    name = models.CharField(max_length=256)
    class_name = models.CharField(max_length=256)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})
