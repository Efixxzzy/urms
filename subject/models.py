from django.db import models

# Create your models here.
class Stream(models.Model):
    branch = models.CharField(max_length=80)
    semester = models.IntegerField()

    def __str__(self):
        return self.branch + " - " + str(self.semester) + " SEM"

class Subject(models.Model):
    code = models.CharField(max_length=8)
    type = models.CharField(max_length=20, choices=(
        ('Regular', 'Regular'),
        ('Re-register', 'Re-register')
    ))

    stream = models.ForeignKey("Stream", on_delete=models.CASCADE)
    courses_offerred = models.ManyToManyField("Course")
    

    def __str__(self):
        return self.code

class Course(models.Model):
    code = models.CharField(max_length=8)
    title = models.CharField(max_length=80)
    credits = models.IntegerField()
    professor = models.CharField(max_length=80)

    stream = models.ForeignKey("Stream", on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " - " + self.title + " - " + str(self.credits) + " credits" + " - " + self.professor

