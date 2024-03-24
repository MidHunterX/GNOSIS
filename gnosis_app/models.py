from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):

    # ISO 639-1 Standard
    LANGUAGES = (
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('ml', 'Malayalam'),
    )

    DEPARTMENTS = (
        ('gen', 'General'),
        ('cse', 'Computer Science and Engineering'),
        ('eee', 'Electrical and Electronics Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ce', 'Civil Engineering'),
        ('ece', 'Electronics and Communication Engineering'),
        ('che', 'Chemical Engineering'),
        ('bt', 'Biotechnology'),
        ('it', 'Information Technology'),
        ('ae', 'Aeronautical Engineering'),
        ('ae', 'Automobile Engineering'),
        ('ie', 'Industrial Engineering'),
        ('mse', 'Materials Science and Engineering'),
        ('ne', 'Nuclear Engineering'),
        ('pe', 'Petroleum Engineering'),
        ('mn', 'Mining Engineering'),
        ('oe', 'Ocean Engineering'),
        ('bce', 'Biochemical Engineering'),
        ('ie', 'Instrumentation Engineering'),
        ('se', 'Systems Engineering'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User , related_name='blog_posts' , on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    likes = models.ManyToManyField(User , related_name='post_likes',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=10 , choices=LANGUAGES,default='en')
    department = models.CharField(max_length=100 , choices=DEPARTMENTS,default='gen')
    restrict_comments = models.BooleanField(default=False)
    favourite_ques = models.ManyToManyField(User,related_name='favourite_ques',blank=True)

    def __str__(self):
        return self.title



class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    DOB = models.DateField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return "profile {}".format(self.user.username)



class Comment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    ques = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='ques_comment')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.ques.title , self.user.username)



class Replies(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_reply')
    comment = models.ForeignKey(Comment , on_delete=models.CASCADE,related_name='comment_reply')
    ques = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='ques_reply')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.comment.id,self.ques.title,self.user.username)
