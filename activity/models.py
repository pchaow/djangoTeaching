from django.db import models

# Create your models here.
ACTIVITY_TYPES = [
    ('AC', 'ACADEMIC'),
    ('SA', 'STUDENT AFFAIR'),
    ('CU', 'CULTURAL'),
]


class Student(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.code} - {self.name}'


class Activity(models.Model):
    class Meta:
        verbose_name_plural = "Activities"

    activity_name = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=2, choices=ACTIVITY_TYPES)
    activity_desc = models.TextField(blank=True, null=True)
    activity_date = models.DateTimeField(auto_now_add=True)  # วันที่สร้างกิจกรรมขึ้นมาในระบบ

    participant = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.activity_name} - {self.activity_date}'

    pass


class ActivityTimeline(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    activity_start = models.DateTimeField()
    activity_stop = models.DateTimeField(blank=True, null=True)
    activity_plantitle = models.CharField(max_length=255)
