from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):    
    q_title = models.CharField(max_length=200)
    question = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    q_date = models.DateTimeField('data published')
    q_photo = models.ImageField(upload_to = 'q_images/', blank =True ,null = True)
    hashtags = models.ManyToManyField('main.Hashtag' , blank = True)
    q_like = models.ManyToManyField(User,related_name ='q_like_users' , blank = True)
    q_like_count = models.PositiveIntegerField(default = 0)
    q_clicks = models.PositiveIntegerField(default=0, verbose_name='QnA_조회수')
    
    def __str__(self):
        return self.q_title

    def q_summary(self) : 
        return self.q_title[:15]

    @property
    def q_update_counter(self) :
        self.q_clicks += 1 
        self.save() 

class Answer(models.Model) :
    def __str__(self) :
        return self.text
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    qna_id = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='answers') 
    text = models.TextField(max_length=50)
    create_at = models.DateTimeField(auto_now=True)
    a_photo = models.ImageField(upload_to = 'a_images/', blank =True ,null = True)
    a_parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null = True) 
