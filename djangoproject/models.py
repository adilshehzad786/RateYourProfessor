from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify

class Post(models.Model):
    UCP='University of Central Punjab  '
    LMDC='Lahore Medical And Dental College'
    POOR='Poor'
    AVERAGE='Average'
    GOOD='Good'
    VERY_GOOD='Very Good'
    EXCELLENT='Excellent'
    BSCS='Bachelor of Computer Science'
    BSSE='Bachelor of Software Engineering'

    Rating_CHOICES = (
        (POOR, 'Poor'),
        (AVERAGE, 'Average'),
        (GOOD, 'Good'),
        (VERY_GOOD, 'Very Good'),
        (EXCELLENT, 'Excellent')
    )
    DEPARTMENT_CHOICES=(
        (BSCS,'Bachelor of Computer Science')  ,
        (BSSE,'Bachelor of Software Engineering'),

    )
    INSTITUTE_CHOICES=(
        (UCP,'University of Central Punjab  '),
        (LMDC, 'Lahore Medical And Dental College'),
    )

    instructor=models.CharField(max_length=100)
    rating=models.CharField(choices=Rating_CHOICES, default=POOR,max_length=10)
    comments=models.TextField()
    institute=models.CharField(choices=INSTITUTE_CHOICES,max_length=50,default=UCP)
    course=models.CharField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    instructor_image=models.ImageField(default = 'default.jpg', upload_to = 'instructor_images/' )
    department=models.CharField(choices=DEPARTMENT_CHOICES,default=BSCS,max_length=50)
    agree_condition= models.BooleanField(default=False)

    def __str__(self):
        return self.instructor

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=100)
    question_text = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.TextField(max_length=20)
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        def __init__(self, *args, **kwargs):
            super(Question, self).__init__(*args, **kwargs)


class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.TextField(max_length=20)
    

