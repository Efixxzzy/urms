from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey("auth.user", on_delete=models.CASCADE)

    name = models.CharField(max_length=80)
    roll_no = models.CharField(max_length=12)
    date_of_birth = models.DateField()
    address = models.TextField()
    contact_number = models.BigIntegerField()

    stream = models.ForeignKey("subject.Stream", on_delete=models.CASCADE)
    courses = models.ManyToManyField("subject.Course", null=True, blank=True)
    locked = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no
