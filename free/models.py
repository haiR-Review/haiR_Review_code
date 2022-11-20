from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#자유게시판 
class Free(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    p_title = models.CharField(max_length=200)
    p_date = models.DateTimeField('data published')
    p_body = models.TextField()
    p_photo = models.ImageField(upload_to='images/', blank = True)
    hashtags = models.ManyToManyField('main.Hashtag', blank = True, null=True, editable=True)
    p_clicks = models.PositiveIntegerField(default=0, verbose_name='자유_조회수')
    p_like = models.ManyToManyField(User,related_name ='f_like_users' , blank = True)
    p_like_count = models.PositiveIntegerField(default = 0)
    
    def __str__(self) : 
        return self.p_title

    def p_summary(self) :
        return self.p_title[:15]
    
    @property
    def p_update_counter(self) :
        self.p_clicks += 1 
        self.save() 


#댓글
class p_comment(models.Model) :
    def __str__(self) :
        return self.text
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    p_id = models.ForeignKey(Free, on_delete=models.CASCADE, null=True, related_name='p_comments')
    text = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=True)
    p_parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null = True) 

