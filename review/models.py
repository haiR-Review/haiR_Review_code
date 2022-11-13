from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# 리뷰게시판
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    r_title = models.CharField(max_length=200)
    r_body = models.TextField()
    hashtags = models.ManyToManyField('main.Hashtag', blank = True)
    r_location = models.CharField(max_length=20, null = True, blank = True)
    r_photo = models.ImageField(upload_to='images/', blank = True)
    r_receipt = models.ImageField(upload_to='images/', blank = True)
    r_nickname = models.CharField(max_length=20, null = True, blank = True)
    r_clicks = models.PositiveIntegerField(default=0, verbose_name='리뷰_조회수')
    r_date = models.DateTimeField('data published')
    r_like = models.ManyToManyField(User,related_name ='r_like_users' , blank = True)
    r_like_count = models.PositiveIntegerField(default = 0)
    
    def __str__(self):
        return self.r_title

    def r_summary(self) : 
        return self.r_title[:20]

    @property
    def r_update_counter(self) :
        self.r_clicks += 1 
        self.save() 


class r_comment(models.Model) :
    def __str__(self) :
        return self.text
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    r_id = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='r_comments')
    text = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=True)
    r_parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null = True) 

