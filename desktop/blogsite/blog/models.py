from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
#post sections 
class Post(models.Model):
    title = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    published_on = models.DateTimeField(auto_now = True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 0)
    blog_image = models.ImageField(upload_to="static", null=True, blank=True,)
   


class Meta :
    ordering = ['-published_on']


def __str__ (self):
    return self.title


# comments section 
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject =models.CharField(max_length=100, null=True, blank=True,)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='replies')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')


    class Meta:
        ordering = ['created_on']
        
    class Meta:
        verbose_name_plural = "Reply"
        
    def __str__(self):
        return 'Reply {} by {}'.format(self.body, self.name)
    

    
#contacts section 
class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_rec = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name + "-" +  self.email



# class Preferences(models.Model):
#     pref = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='pref')
#     likes= models.IntegerField(default=0)
#     dislikes= models.IntegerField(default=0)
#     date= models.DateTimeField(auto_now_add= True)
#     class Meta:
#         ordering = ['-date']

#     class Meta:
#         verbose_name_plural = "Preference"
