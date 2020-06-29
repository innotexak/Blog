from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
#post sections 
class Posts(models.Model):
    title = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    posted_on = models.DateTimeField(auto_now = True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default = 0)


class Meta :
    ordering = ['-created_on']


def __str__ (self):
    return self.title


#comments section 
class Comment(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

#contacts section 
class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']

    class Meta:
        verbose_name_plural = "Feedback"
 
    def __str__(self):
        return self.name + "-" +  self.email



class Preferences(models.Model):
    pref = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='pref')
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    date= models.DateTimeField(auto_now_add= True)
    class Meta:
        ordering = ['-date']

    class Meta:
        verbose_name_plural = "Prefereces"

# class About(models.Model):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     written_on = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['-written_on']
    
#     class Meta:
#         verbose_name_plural = "About"