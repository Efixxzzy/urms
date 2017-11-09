from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey("auth.user", on_delete=models.CASCADE)

    name = models.CharField(max_length=80, null=True, blank=True)
    roll_no = models.CharField(max_length=12)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    contact_number = models.BigIntegerField(null=True, blank=True)

    stream = models.ForeignKey("subject.Stream", on_delete=models.CASCADE)
    courses = models.ManyToManyField("subject.Course", null=True, blank=True)
    locked = models.BooleanField(default=False)

    transaction_id = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.roll_no
