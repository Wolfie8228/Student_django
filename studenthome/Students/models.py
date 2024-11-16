from django.db import models

# Create your models here.
class student(models.Model):
    s_id = models.IntegerField(null= False, blank= False)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField(null= False, blank= False)

    def get_pass_or_fail(self):
        return "Pass" if self.marks > 40 else "Fail"