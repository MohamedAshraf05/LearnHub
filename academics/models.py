from django.db import models

# Create your models here.

class Teachers(models.Model):
    
    class Specialization(models.TextChoices):
        MOBILE_APPLICATION = 'MA' , 'Mobile Application'
        WEB_DEVELOPMENT = 'WD' , 'Web Development'
        MATHEMATICS = 'MAs' , 'Maths'

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    academic_specialization = models.CharField(max_length=25 , choices=Specialization.choices)
    Custom_id = models.PositiveIntegerField(unique=True , null=True , blank=True)
    image = models.FileField(upload_to="static/image" , blank=True)
    job_name = models.CharField(max_length=155 , null=True ,blank=True)
    def __str__(self):
         return self.name

    def save(self, *args, **kwargs):
        if self.Custom_id is None:
            last_teacher = Teachers.objects.all().order_by('Custom_id').last()
            if last_teacher:
                self.Custom_id = last_teacher.Custom_id + 1
            else:
                self.Custom_id = 1
        super().save(*args, **kwargs)


class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teachers , on_delete=models.CASCADE , default='')
    image = models.FileField(upload_to='static/image' , blank=True)
    Custom_id = models.PositiveIntegerField(unique=True , null=True , blank=True)


    def save(self, *args, **kwargs):
        if self.Custom_id is None:
            last_course = Courses.objects.all().order_by('Custom_id').last()
            if last_course:
                self.Custom_id = last_course.Custom_id + 1
            else:
                self.Custom_id = 1
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
